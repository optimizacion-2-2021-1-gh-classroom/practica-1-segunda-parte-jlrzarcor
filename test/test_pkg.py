import pytest
import numpy as np
import os

os.chdir("../")
import oa_e5 as oa

a = np.array([[3, 2, -1], [2, -1, 1], [-1, 1, -1]]) #Matrix simétrica
b = np.array([1, -2, 0])
x = np.linalg.solve(a, b)
i3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) #Matrix identidad


def test_cgm():
    x_sol = oa.cgm(a,b,np.array([1,1,1]))
    assert np.linalg.norm(x-x_sol) < 1e-10


def test_its_simetric():
    assert oa.its_simetric(a)


def test_symmetrize():
    syn_mt = oa.symmetrize(4)
    assert oa.its_simetric(syn_mt)
    
def test_is_pos_def():
    assert oa.is_pos_def(i3)

def test_symmetrize_posdef():
    t_spd = oa.symmetrize_posdef(3)
    assert oa.its_simetric(t_spd) and oa.is_pos_def(t_spd)