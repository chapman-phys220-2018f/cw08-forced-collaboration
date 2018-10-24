#!/usr/bin/env python3

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

import sinesum as ss
import numpy.testing as npt

def test_f():
    npt.assert_approx_equal(ss.f(2,0), 0.0, significant=5)
    npt.assert_approx_equal(ss.f(2,0.5), 1.0, significant = 5)
    npt.assert_approx_equal(ss.f(2,-0.5), -1.0, significant = 5)

def test_Sn():
    npt.assert_approx_equal(ss.Sn(2,0.5,100),1, significant = 5)
    npt.assert_approx_equal(ss.Sn(2,-0.5,100),-1, significant = 5)
    npt.assert_approx_equal(ss.Sn(2,0,100), 0 , significant = 5)
    
    