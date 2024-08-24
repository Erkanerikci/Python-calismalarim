import cv2
import numpy as np

dosyayolu = r"C:\Users\erkan\OneDrive\Resimler\CRIXUS.jpg"
resim = cv2.imread(dosyayolu,0)
cv2.imshow("Resim",resim)
cv2.imwrite("Griresim.jpg",resim)

