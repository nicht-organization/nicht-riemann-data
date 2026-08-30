import numpy as np

from nicht_riemann_data.transforms import (
    spacings,
    normalized_spacings,
)


def test_spacings():
    gamma = np.array([1.0, 3.0, 6.0])

    np.testing.assert_allclose(
        spacings(gamma),
        [2.0, 3.0],
    )


def test_normalized_spacings():
    gamma = np.array([1.0, 3.0, 6.0])

    np.testing.assert_allclose(
        normalized_spacings(gamma),
        [0.8, 1.2],
    )


def test_single_value():
    gamma = np.array([42.0])

    assert spacings(gamma).size == 0
    assert normalized_spacings(gamma).size == 0