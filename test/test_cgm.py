import pytest
import numpy as np
import os

os.chdir("../")
import oa_e5 as oa

a = np.array([[3, 2, -1], [2, -1, 1], [-1, 1, -1]])
b = np.array([1, -2, 0])
x = np.linalg.solve(a, b)


def test_cgm():
    x_sol = oa.cgm(a,b,np.array([1,1,1]))
    assert np.linalg.norm(x-x_sol) < 1e-10
    