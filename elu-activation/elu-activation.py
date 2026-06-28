import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    x = np.array(x)

    return list(np.where(x > 0, x, (alpha * (np.exp(x) - 1))))