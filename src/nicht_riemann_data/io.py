from pathlib import Path
import numpy as np


def load_real_zeros(path: str | Path) -> np.ndarray:
    """
    Load imaginary parts gamma_n from a simple text file.

    Expected:
        one gamma value per line
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(path)

    gamma = np.loadtxt(path, dtype=float)

    if gamma.ndim != 1:
        gamma = gamma.reshape(-1)

    return gamma
