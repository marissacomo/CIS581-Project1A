'''
  File name: findDerivatives.py
  Author:
  Date created:
'''

'''
  File clarification:
    Compute gradient information of the input grayscale image
    - Input I_gray: H x W matrix as image
    - Output Mag: H x W matrix represents the magnitude of derivatives
    - Output Magx: H x W matrix represents the magnitude of derivatives along x-axis
    - Output Magy: H x W matrix represents the magnitude of derivatives along y-axis
    - Output Ori: H x W matrix represents the orientation of derivatives
'''
#!/usr/local/bin/python3
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import utils

def findDerivatives(I_gray):

  # Gaussian Filter Definition
  G = [[2.0/159.0, 4.0/159.0, 5.0/159.0, 4.0/159.0, 2.0/159.0], 
       [4.0/159.0, 9.0/159.0, 12.0/159.0, 9.0/159.0, 4.0/159.0], 
       [5.0/159.0, 12.0/159.0, 15.0/159.0, 12.0/159.0, 5.0/159.0],
       [4.0/159.0, 9.0/159.0, 12.0/159.0, 9.0/159.0, 4.0/159.0],
       [2.0/159.0, 4.0/159.0, 5.0/159.0, 4.0/159.0, 2.0/159.0]]

# OUTPUT: Magx & Magy - Find the magnitude of derivatives along x-axis and y-axis
  # Filter out noise and compute derivative (gradient)
  dx, dy = np.gradient(G, axis = (1,0)) 
  Magx = signal.convolve2d(I_gray, dx,'same', boundary = 'symm')
  Magy = signal.convolve2d(I_gray, dy,'same', boundary = 'symm')

# OUTPUT: Mag - Find the magnitude of the derivatives
  # Compute Magnitude of the gradient
  Mag = np.sqrt(Magx*Magx + Magy*Magy);

# OUPUT: Ori - Find the orientation of the edges
  Ori = np.arctan2(Magy, Magx);  # Gradient Angle

  D = [Mag, Magx, Magy, Ori] # [Mag,Magx,Magy,Ori]
  return(D)
