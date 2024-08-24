import cv2
import numpy as np

resim = cv2.imread("tomruk-agac.jpg",0)
cv2.imshow("Resmim",resim)
a = cv2.waitKey(0)
if a == 27:
    cv2.destroyAllWindows()
elif a == ord("s"):
    cv2.imwrite("GriResim.jpg",resim)