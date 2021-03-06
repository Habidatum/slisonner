import numpy as np
from tempfile import NamedTemporaryFile


def generate_slice(x_size, y_size, value_type):
    random_slice = np.random.rand(x_size, y_size) * 10
    random_slice = random_slice.astype(value_type)
    random_slice[x_size-1][y_size-1] = np.nan
    temp = NamedTemporaryFile(delete=False)
    random_slice.tofile(temp)
    return temp.name
