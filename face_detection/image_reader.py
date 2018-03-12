from skimage import io
from imutils import resize, url_to_image


def read_image(path, width=None):
    image = io.imread(path)
    if width:
        image = resize(image, width=width)
    return image


def read_url(url, width=None):
    image = url_to_image(url)
    if width:
        image = resize(image, width=width)
    return image


def read_string(str, width=None):
    image = io.imread(str, plugin='imageio')
    if width:
        image = resize(image, width=width)
    return image
