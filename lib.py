import cv2 as cv
import numpy as np
import argparse as argp
import enum

from ramp import Ramp
from algorithm import *

class Algorithm(enum.Enum):
    NORMALIZE = "NORMALIZE"

def csv_to_tuple(csv: str) -> tuple:
    csv = csv.replace(" ", "")
    return tuple (
        map (
            int, csv.split(',')
        )
    )

def parse_ramp(ramp_name: str) -> str:
    return Ramp.__members__[ramp_name].value

def parse_algorithm(algo_name: str):
    return {
        Algorithm.NORMALIZE.name: normalize
    }[algo_name]

def resize_image(image: np.ndarray, size: int) -> np.ndarray:
    im_shape = image.shape
    transform = np.divide(size, np.max(im_shape))
    resized_shape = np.multiply(im_shape, transform).astype(int)
    resized_shape = resized_shape[::-1] #flip resolution
    return cv.resize(image, resized_shape)

def set_image_resolution(image, resolution):
    return cv.resize(image, resolution)

arg_parser = argp.ArgumentParser(description="convert image to ascii art")
arg_parser.add_argument(
    "-p", "--path", type=str,
    help="specify target file path", 
    required=True
)
arg_parser.add_argument(
    "-e", "--encoding", type=str,
    help="set pixel data encoding scheme (Ramp)",
    default=Ramp.BASE10.name, required=False
)
arg_parser.add_argument(
    "-a", "--algorithm", type=str,
    help="specify algorithm to use",
    default=Algorithm.NORMALIZE.value, required=False
)
arg_parser.add_argument(
    "-s", "--size", type=int,
    help="scales the max image resolution to the specified size, preserving aspect ratio",
    default=None, required=False
)
arg_parser.add_argument(
    "-r", "--resolution", type=str,
    help="sets the resolution of the image, accepts CSV format",
    default=None, required=False
)
arg_parser.add_argument(
    "-o", "--output", type=str,
    help="specify output path", 
    default=False, required=False
)
arg_parser.add_argument(
    "-i", "--inverted", action="store_true",
    help="invert encoding scheme",
    required=False
)
arg_parser.add_argument(
    "--disable_print", action="store_true",
    help="don't output result to console",
    required=False
)