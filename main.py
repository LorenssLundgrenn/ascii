from ascii_lib import *

# need a proper command-line interface (argparse lib)
source = "sample/dog.jpg"
size = 80

out = img_to_ascii(source, Ramp.base10, scale=80)
print(out)
with open("out.txt", "wt") as f:
    f.write(out)
