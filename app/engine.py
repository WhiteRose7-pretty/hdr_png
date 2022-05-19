import cv2
import numpy as np
import os

def convert_hdr(hdr_path):
    hdr = cv2.imread(hdr_path, flags=cv2.IMREAD_ANYDEPTH)
    ldr = np.clip(hdr, 0, 1)
    # Color space conversion
    ldr = ldr ** (1 / 2.2)
    # 0-255 remapping for bit-depth conversion
    ldr = 255.0 * ldr

    ldr_path = os.path.splitext(hdr_path)[0] + '.png'
    cv2.imwrite(ldr_path, ldr)

    return ldr_path

