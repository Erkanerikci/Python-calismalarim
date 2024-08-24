import cv2
import numpy as np

cap = cv2.VideoCapture("yurii boyka.mp4")

while (cap.isOpened()):
    deger, kare = cap.read()
    gray = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video",gray)

    if cv2.waitKey(1) & 0xFF == ord("q") :
        break


cap.release()
cv2.destroyAllWindows()