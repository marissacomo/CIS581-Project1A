'''
  File name: edgeLink.py
  Author:
  Date created:
'''

'''
  File clarification:
    Use hysteresis to link edges based on high and low magnitude thresholds
    - Input M: H x W logical map after non-max suppression
    - Input Mag: H x W matrix represents the magnitude of gradient
    - Input Ori: H x W matrix represents the orientation of gradient
    - Output E: H x W binary matrix represents the final canny edge detection map

Basically we move all the weak edge pixels in their edge direction. And if any pixel lands on a strong edge, then we make that weak pixel a strong pixel.

Then, we iterate this a fixed amount of times

So, the weak pixels start becoming strong pixels 1 jump at a time

Nidhi did mention about doing some fixed "hops" im not sure

Also, we can make the edge direction discrete so we can access +1 -1 in X Y
I did ask for diagonal another TA said its fine to do it in orthogonal axis
'''
#!/usr/local/bin/python3
import numpy as np
import utils
import matplotlib.pyplot as plt
import helpers

def edgeLink(M, Mag, Ori):
# - Thresholds for weak edges & strong edges -
  threshold_low = np.median(Mag)
  threshold_high = np.median(Mag) + (np.std(Mag))
  
  strong_edge_map = np.multiply(M, np.greater(Mag, threshold_high))
  weak_edge_map = np.multiply(M, np.logical_and(Mag > threshold_low, Mag < threshold_high))
 
# 1) make a mesh grid of all pixel locations
  nr = Mag.shape[0];
  nc = Mag.shape[1];
  X, Y = np.meshgrid(np.arange(nc), np.arange(nr))
  
  for x in range(1,2):    
    
    weak_edge_map = np.logical_xor(weak_edge_map, np.logical_and(weak_edge_map, strong_edge_map))
# 2) use the orientation to compute the offset forward and back for each pixel
    delta_xb = x * (np.cos(Ori - np.pi/2)) # delta back x-pixel
    delta_xf = x * (np.cos(Ori + np.pi/2)) # delta forward x-pixel
    delta_yb = x * (np.sin(Ori - np.pi/2)) # delta backward y-pixe
    delta_yf = x * (np.sin(Ori + np.pi/2)) # delta forward y-pixel

# 3) make a comparison pixel locations for forward and back for all pixel locations
    xf = np.multiply(delta_xf, weak_edge_map) + X
    xb = np.multiply(delta_xb, weak_edge_map) + X
    yf = np.multiply(delta_yf, weak_edge_map) + Y
    yb = np.multiply(delta_yb, weak_edge_map) + Y

    for y in range(20):
# 4) use weak_edge_map's orientation to see if there is a strong edge in its neighborhood 
      Hb = helpers.hysteria(strong_edge_map, xb, yb)
      Hf = helpers.hysteria(strong_edge_map, xf, yf)
      strong_edge_map = np.logical_or(strong_edge_map, Hb)
      strong_edge_map = np.logical_or(strong_edge_map, Hf)
  return(strong_edge_map)
'''plt.figure()
  ax = plt.subplot(221)
  plt.title('Edge Map')
  plt.imshow(M*Mag, cmap='gray')

  plt.subplot(222, sharex=ax, sharey=ax)
  plt.title('Weak Edge Map')
  plt.imshow(weak_edge_map, cmap='gray')
   
  plt.subplot(223, sharex=ax, sharey=ax)
  plt.title('orig_strong_edge_map')
  plt.imshow(orig_strong_edge_map, cmap='gray')

  plt.subplot(224, sharex=ax, sharey=ax)
  plt.title('strong_edge_map')
  plt.imshow(strong_edge_map, cmap='gray')

  plt.show()
'''
  
