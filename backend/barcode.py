import cv2
import numpy as np
from pyzbar.pyzbar import decode

def scan_barcode(image):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    barcodes = decode(gray)

    for barcode in barcodes:
        return barcode.data.decode("utf-8")

    return None