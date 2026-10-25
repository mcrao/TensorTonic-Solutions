import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    np_x = np.asarray(x, dtype=float)
    np_y = np.asarray(y, dtype=float)

    return float(np.dot(np_x, np_y)) # can also use float(np.sum(np_x * np_y)) if direct np.dot is not allowed