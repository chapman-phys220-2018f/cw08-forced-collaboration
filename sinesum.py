#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########
#Name: Conner Carnahan
#ID: 1614309
#Email: carna104@mail.chapman.edu
#Class: PHYS220
#Date: Oct 16, 2018
########

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

@np.vectorize
def Sn(T,t,n):
    """sumsinefunc(float T,float t,int n): Returns a value computed by a sum of sin functions in accordance with the Fourier series expansion of sign(x)"""
    if (abs(t) > T/2):
        print("t should be within the range -T/2, T/2")
        pass
    K = np.arange(1,n+1)
    K = np.divide(4,np.pi*(2*K-1))
    SinPeriods = np.divide(2*np.pi*(2*np.arange(1,n+1)-1),T)
    value = np.sum(K*np.sin(SinPeriods*t))
    return value

@np.vectorize
def f(T,t):
    """f(float T, float t): Returns a value that is the sign of the value inputed
       if t < 0 sign(t) = -1
       if t > 0 sign(t) = 1
       if t = 0 sign(t) = 0"""
    if (abs(t) > T/2):
        print("t should be between T/2")
        pass
    return np.sign(t)

def Snarray(T,n,K = 300):
    Time = np.linspace(-T/2,T/2,K)
    return Sn(T,Time,n)

def farray(T,K = 300):
    Time = np.linspace(-T/2,T/2,K)
    return f(T,Time)

def timespace(T,K = 300):
    return np.linspace(-T/2,T/2,K)

###
def buildallplots(alpha):
    """args: alpha (float),
       returns null
       This is a helper function that takes in a float, alpha,
       and generates a sequence of partial Fourier Sums that approximate the sign function"""
    T = alpha*2*np.pi
    F1Array = ss.Snarray(T,1)
    F3Array = ss.Snarray(T,3)
    F5Array = ss.Snarray(T,5)
    F10Array = ss.Snarray(T,10)
    F30Array = ss.Snarray(T,30)
    F100Array = ss.Snarray(T,100)
    FuncArray = ss.farray(T)
    Time = ss.timespace(T)
###