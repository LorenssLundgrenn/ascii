import os
import time
import cv2

import lib

if (__name__ == "__main__"):
    args = lib.arg_parser.parse_args()
    if not os.path.exists(args.path):
        raise ValueError(f"could not find path {args.path}")

    image = cv2.imread(args.path, cv2.IMREAD_GRAYSCALE)
    ramp = lib.parse_ramp(args.encoding)
    algorithm = lib.parse_algorithm(args.algorithm)

    if (args.size):
        image = lib.resize_image(image, args.size)
    elif (args.resolution):
        resolution = lib.csv_to_tuple(args.resolution)
        image = lib.set_image_resolution(image, resolution)
    if (args.inverted):
        ramp = ramp[::-1]

    char_buffer = ""
    timestamp = time.time()

    ascii_str = algorithm(image=image, ramp=ramp)
    if (not args.disable_print): 
        char_buffer += ascii_str + "\n"
    if (args.output): 
        out = args.output
        if (not '.' in out): out += ".txt"
        with open(out, "wt") as f: f.write(ascii_str)
        char_buffer += f"wrote to file: {args.output} | "

    elapsed_time = time.time() - timestamp
    print(char_buffer + f"elapsed processing time: {elapsed_time}ms")