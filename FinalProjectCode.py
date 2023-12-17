# specify the binary file path below
from kmeans import *
# import required libraries
import struct
import sys
import serial
import binascii
import time
import numpy as np
import math

import os
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs


# Local File Imports
from parse_bin_output import *

binDirPath = ""
output_dict = parse_ADC(binDirPath)
print(f"\neach frame dict contains following informations: {output_dict[0].keys()}")

def convert_range_profile_to_distances(range_profile, fs=100e6/8, c0=3e8, S=170e12, num_ADC=256):
    nFFT = len(range_profile)     # number of FFT bins
    sam_perd = 1/fs
    chirp_dur = sam_perd * num_ADC
    bandwidth = S * chirp_dur
    Dres = c0 / (2 * bandwidth)
    dmax = (fs * c0) / (2 * S)
    delta_d = dmax / nFFT
    
    # vRange represents the distance vector
    vRange = np.arange(nFFT) * delta_d
    vRange = vRange[:len(range_profile)]
    
    # Convert range profile to distances
    distances = np.array(range_profile) * Dres
    
    return vRange, min(distances)# sum(distances) / len(distances)

# Example usage:
frame_num = 0
range_profile = output_dict[frame_num]['rangeProfile']

# Convert range profile to distances
outputs = []
for i in range(len(output_dict)):
    range_profile = output_dict[i]['rangeProfile']
    vRange, dist = convert_range_profile_to_distances(range_profile)
    outputs.append(dist)
outputs = [40 - x/float(4) for x in outputs]
print("Vertical Jump",max(outputs) - min(outputs))
plt.plot(outputs)
plt.xlabel('Frames')
plt.ylabel('Dist from radar')
plt.title('Plot of the List Data')

# Show the plot
plt.show()
