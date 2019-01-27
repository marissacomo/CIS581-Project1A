'''
  File name: helpers.py
  Author:
  Date created:
'''

'''
  File clarification:
    Helpers file that contributes the project
    You can design any helper function in this file to improve algorithm
'''
 #!/usr/bin/env python3
import numpy as np

def hysteria(v, xq, yq):
  q_h = xq.shape[0]
  q_w = xq.shape[1]

  xq = xq.flatten()
  yq = yq.flatten()

  h = v.shape[0]
  w = v.shape[1]

  x_floor = np.floor(xq).astype(np.int32)
  y_floor = np.floor(yq).astype(np.int32)
  x_ceil = np.ceil(xq).astype(np.int32)
  y_ceil = np.ceil(yq).astype(np.int32)

  x_floor[x_floor<0] = 0
  y_floor[y_floor<0] = 0
  x_ceil[x_ceil<0] = 0
  y_ceil[y_ceil<0] = 0

  x_floor[x_floor>=w-1] = w-1
  y_floor[y_floor>=h-1] = h-1
  x_ceil[x_ceil>=w-1] = w-1
  y_ceil[y_ceil>=h-1] = h-1
       
  v1 = v[y_floor, x_floor]
  v2 = v[y_floor, x_ceil]
  v3 = v[y_ceil, x_floor]
  v4 = v[y_ceil, x_ceil]

  log1 = np.logical_or(v1, v2)
  log2 = np.logical_or(v3, v4)
  result = np.logical_or(log1, log2)

  return(result.reshape(q_h,q_w))
