from __future__ import annotations

import numpy as np


def describe(x: np.ndarray) -> dict[str, float]:
    x = np.asarray(x, dtype=float)

    if x.size == 0:
        return {
            "n": 0,
            "min": float("nan"),
            "max": float("nan"),
            "mean": float("nan"),
            "std": float("nan"),
        }

    return {
        "n": int(x.size),
        "min": float(np.min(x)),
        "max": float(np.max(x)),
        "mean": float(np.mean(x)),
        "std": float(np.std(x)),
    }
