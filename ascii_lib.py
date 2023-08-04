import cv2 as cv
import numpy as np
import enum

class Ramp(enum.Enum):
    base10 = '@%#*+=-:. '
    base70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# map pixel brightness to ascii, divide pixel data by largest pixel value
# multiply quotient matrix by max ramp index, derive str matrix from indices
def brightness_algorithm(image, ramp):
    ramp_indices = (len(ramp) - 1)
    max_quotient = image.astype(float) / np.max(image)
    derived_indices = (max_quotient * ramp_indices).astype(int)

    mapped_matrix = np.array(list(ramp))[derived_indices]
    str2d = '\n'.join(' '.join(row) for row in mapped_matrix)
    return str2d

def img_to_ascii(fname, ramp, 
    scale=None, 
    set_size=None,
    algorithm=brightness_algorithm, 
    inverted=False
):
    image = cv.imread(fname, cv.IMREAD_GRAYSCALE)
    im_shape = image.shape
    if ( scale ):
        transform = np.divide(scale, np.max(im_shape))
        resized_shape = np.multiply(im_shape, transform).astype(int)
        flip_resolution = resized_shape[::-1]
        image = cv.resize(image, flip_resolution)
    elif ( set_size ):
        image = cv.resize(image, set_size)
        
    ramp = ramp.value[::-1]
    if ( inverted ): ramp = ramp[::-1]
    return algorithm(image, ramp)