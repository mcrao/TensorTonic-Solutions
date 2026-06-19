import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    np_x = np.array(x)
    
    return np.where(
        np_x >= 0,
        1 / (1 + np.exp(-np_x)),
        np.exp(np_x) / (1 + np.exp(np_x))
    )