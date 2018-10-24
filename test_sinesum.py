#!/usr/bin/env python3

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

import sinesum as ss
import numpy.testing as npt

def test_f():
    """test_f: tests the f function, this checks that it outputs -1 if x < 0 , 0 if x = 0, 1 if x > 0, up to certain significant digits (else we would have problems testing floats)"""
    npt.assert_approx_equal(ss.f(2,0), 0.0, significant=2)
    npt.assert_approx_equal(ss.f(2,0.5), 1.0, significant = 2)
    npt.assert_approx_equal(ss.f(2,-0.5), -1.0, significant = 2)

def test_Sn():
    """test_Sn: tests if Sn is approximating the sign function up to 2 significant digits after 100 terms have been summed"""
    npt.assert_approx_equal(ss.Sn(2,0.5,100),1, significant = 2)
    npt.assert_approx_equal(ss.Sn(2,-0.5,100),-1, significant = 2)
    npt.assert_approx_equal(ss.Sn(2,0,100), 0 , significant = 2)
    
    