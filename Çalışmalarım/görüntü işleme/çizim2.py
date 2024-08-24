import cv2
import numpy as np

resim = cv2.imread("Griresim.jpg")
cv2.imshow("Pencere",resim)

resim2 = cv2.rectangle(resim,(15,15),(512,512),(0,255,0),6) # Kare veya dikdörtgen çizme
cv2.imshow("Pencere2",resim2)

resim3 = cv2.circle(resim2,(450,150),40,(0,0,255),-1) # Yuvarlak çizme
cv2.imshow("Pencere3",resim3)
font = cv2.FONT_HERSHEY_COMPLEX
resim4 = cv2.putText(resim,"CRIXUS",(00,150),font,7,(0),8,cv2.LINE_AA) # Yazı yazma
cv2.imshow("Pencere2",resim4)

cv2.waitKey(0)
cv2.destroyAllWindows()