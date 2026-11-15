import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    np_a = np.asarray(a, dtype=float)
    np_b = np.asarray(b, dtype=float)
    norm_a = np.linalg.norm(np_a)
    norm_b = np.linalg.norm(np_b)

    return 0.0 if norm_a == 0 or norm_b == 0 else float(np.dot(np_a, np_b) / (norm_a * norm_b))

    pass