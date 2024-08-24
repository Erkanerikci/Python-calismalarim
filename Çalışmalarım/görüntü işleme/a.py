import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükleme
img = cv2.imread('Maskeli.jpg')

# Görüntüyü griye dönüştürme
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Eşikleme (Thresholding) işlemi
_, thresholded = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)

# Gürültüyü azaltmak için Gaussian bulanıklığı
blur = cv2.GaussianBlur(thresholded, (9, 9), 2)

# Kenar tespiti için Canny algoritmasını uygulama
edges = cv2.Canny(blur, 50, 150)

# Hough dönüşümü ile daireleri bulma
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=60,
                           param1=50, param2=30, minRadius=30, maxRadius=60)

# Daireler varsa işlemleri yapma
if circles is not None:
    circles = np.uint16(np.around(circles))
    print(f"Bulunan daire sayısı: {len(circles[0])}")
    for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]

        # Radius değerine göre filtreleme
        if 20 <= radius <= 60:
            # Dairenin merkezini ve yarıçapını alarak çizme
            cv2.circle(img, center, radius, (0, 255, 0), 2)
            cv2.circle(img, center, 2, (0, 0, 255), 3)
else:
    print("Hiç daire bulunamadı.")

# Maske ve tespit edilen dairelerin gösterimi
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Maske")
plt.imshow(thresholded, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Daire Tespiti")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
