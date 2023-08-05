import numpy as np

# map pixel brightness to ascii, divide pixel data by largest pixel value
# multiply quotient matrix by max ramp index, derive str matrix from indices
def normalize(image: np.ndarray, ramp: str) -> str:
    ramp_indices = (len(ramp) - 1)
    max_quotient = image.astype(float) / np.max(image)
    derived_indices = (max_quotient * ramp_indices).astype(int)

    mapped_matrix = np.array(list(ramp))[derived_indices]
    ascii = '\n'.join(' '.join(row) for row in mapped_matrix)
    return ascii