import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    deger, kare = cap.read()
    cv2.imshow("Video",kare)

    if cv2.waitKey(1) & 0xFF == ord("q") :
        break

cap.release()
cv2.destroyAllWindows()