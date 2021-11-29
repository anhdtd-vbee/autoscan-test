from __future__ import absolute_import

import os
import sys

from my_lib import Object, Object2, Object3
from third_party import (
    lib1,
    lib2,
    lib3,
    lib4,
    lib5,
    lib6,
    lib7,
    lib8,
    lib9,
    lib10,
    lib11,
    lib12,
    lib13,
    lib14,
    lib15,
)

print("Hey")
print("yo")


def my_func():
    return None


def calculate_something(a, b, c, d, e, f, g, h):
    i = a + b
    j = (c + d) / 2
    k = e * f
    m = g - h
    # Check if i is an odd number
    if (i % 2) == 1:
        i += 1
    return i + j + k + m
