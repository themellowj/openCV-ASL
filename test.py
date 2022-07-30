import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time
 
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
 