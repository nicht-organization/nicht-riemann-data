from __future__ import annotations

import numpy as np


def spacings(gamma: np.ndarray) -> np.ndarray:
    """Return consecutive differences gamma[n+1] - gamma[n]."""
    gamma = np.asarray(gamma, dtype=float)

    if gamma.ndim != 1:
        raise ValueError("gamma must be one-dimensional")

    if len(gamma) < 2:
        return np.array([], dtype=float)

    return np.diff(gamma)


def normalized_spacings(gamma: np.ndarray) -> np.ndarray:
    """
    Normalize consecutive zero spacings by their arithmetic mean.
    """
    delta = spacings(gamma)

    if len(delta) == 0:
        return delta

    mean = np.mean(delta)

    if mean == 0:
        raise ValueError("mean spacing must not be zero")

    return delta / mean
