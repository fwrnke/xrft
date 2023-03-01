"""
Insert short description.

@author: fwrnke
@email:  fwrnke@mailbox.org, fwar378@aucklanduni.ac.nz
@date:   2023-02-23

"""
import os

import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt

import xrft

#%% MAIN

if __name__ == '__main__':
    
    fig, ax = plt.subplots(2, 1, figsize=(12, 8))
    
    # sampling rate
    sr = 2000
    # sampling interval
    ts = 1.0 / sr
    t = np.arange(0, 1, ts)
    
    freq = 1.
    x = 3*np.sin(2*np.pi*freq*t)
    
    freq = 4
    x += np.sin(2*np.pi*freq*t)
    
    freq = 7
    x += 0.5* np.sin(2*np.pi*freq*t)
    
    ax[0].plot(t, x, 'r-')
    
    
    for n in range(sr, sr * 2, 500):
        fwd = np.fft.rfft(x, n=n)
        freq = np.fft.rfftfreq(n, d=ts)
        # if len(f) % 2 == 0:
        #     freq = np.abs(f[0:int(n / 2 + 1)])
        # else:
        #     freq = f[0:n / 2 + 1]
        
        ax[1].plot(freq, np.abs(fwd), label=f'npts: {sr}, n: {n}')
        # break
        
    ax[1].legend()
        
    
