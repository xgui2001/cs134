"""A program to recolor images by clustering related colors.
Use in the following way:
    python3 recolor.py image-name.png k
image-name defaults to 'Bedroom.png'; k defaults to 8.
The result will appear in Result-{k}.png.
"""
from PIL import Image, ImageDraw  # From the 'pillow' extension
import cluster                    # Lab 6 clustering code

__all__ = ('Color', 'colorDist', 'colorMean', 'WHITE', 'BLACK', 'Recolor')

def _clamp(value):
    """Clamp value to integer in 0...255."""
    result = int(round(value))
    if result < 0:
        result = 0
    if result > 255:
        result = 255
    return result

def colorMean(colors):
    """Compute the (clamped) mean of a sequence of colors."""
    assert  colors
    rsum,gsum,bsum = 0,0,0
    n = 0
    for (r,g,b) in colors:
        rsum += r
        gsum += g
        bsum += b
        n += 1
    rmean = _clamp(rsum/n)
    gmean = _clamp(gsum/n)
    bmean = _clamp(bsum/n)
    return (rmean, gmean, bmean)

def colorDist(c0, c1):
    """Compute the (squared) distance between two colors."""
    dr = c0[0] - c1[0]
    dg = c0[1] - c1[1]
    db = c0[2] - c1[2]
    return (dr*dr + dg*dg + db*db)**0.5

class Color(object):
    """An immutable class defining a color using the RGB color model."""
    __slots__ = [ '_rgb' ]

    def __init__(self, c):
        """Construct a color from RGB tuple."""
        self._rgb = (_clamp(c[0]), _clamp(c[1]), _clamp(c[2]))

    @property
    def red(self):
        """Return red component."""
        return self._rgb[0]

    @property
    def green(self):
        """Return green component."""
        return self._rgb[1]

    @property
    def blue(self):
        """Return blue component."""
        return self._rgb[2]

    @property
    def rgb(self):
        """Return RGB color values."""
        return self._rgb

    def hash(self):
        """Return a hash code for a color; colors are immutable."""
        return hash(self._rgb)

    def __eq__(self,other):
        """Determine if two colors are equal."""
        return self._rgb == other._rgb

    def __str__(self):
        """A string representation of this color."""
        return str(self.rgb)

    def __repr__(self):
        """The eval-able representation of this color."""
        return "Color({})".format(self.rgb)

# Classic colors:
WHITE = Color( (255,255,255) )
BLACK = Color( (0,0,0) )

class Recolor(object):
    """Recolor a .png image using 'k' colors.  Makes use of a clustering
    of 'k' values."""
    __slots__ = ['_width', '_height', '_image', '_px', '_clust']

    def __init__(self,img, k=8):
        self._image = img
        self._width,self._height = img.size
        self._px = img.load()
        # here, we cluster based on unique r-g-b tuples that represent the colors
        pixels = list({ self._px[x,y][:3]
                  for y in range(self.height) for x in range(self.width)})
        self._clust = cluster.Clustering(pixels, k, colorDist, colorMean, verbose=True)

    @property
    def width(self):
        """The width of the image produced by this filter."""
        return self._width

    @property
    def height(self):
        """The height of the image produced by this filter."""
        return self._height

    def before(self,x,y):
        """Access to pixels this filter is based on."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return Color(self._px[x,y][:3])
        else:
            return WHITE

    def after(self,x,y):
        """Determine the color associated with pixel x,y."""
        # get the pixel color from the input at this (x,y) location
        (r,g,b) = self.before(x,y).rgb
        # the final value is the re-classified color using the clustering
        return Color(self._clust.classify((r,g,b)))

    def image(self):
        """Generate an image from this filter."""
        # create a new, white image.
        i = Image.new("RGB",(self.width,self.height),WHITE.rgb)
        for x in range(i.width):
            for y in range(i.height):
                # draw the remapped pixels onto the image
                ImageDraw.Draw(i).point((x,y),self.after(x,y).rgb)
        return i

if __name__ == "__main__":
    from sys import argv
    imageName = "Bedroom.png"
    k = 8
    if len(argv) >= 2:
        imageName = argv[1]
    if len(argv) >= 3:
        k = int(argv[2])
        
    # read in an image.
    image = Image.open(imageName)

    # generate a new image that has been recolored
    result = Recolor(image,k)

    # save the resulting image in recolored.png
    result.image().save("Result-{}.png".format(k))
