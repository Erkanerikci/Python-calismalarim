import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('T.jpg')

# Görüntüyü HSV renk uzayına dönüştürme
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Kahverengi renk aralığını tanımlama (örnek aralık)
lower_brown = np.array([10, 50, 50])    # Düşük HSV değerleri
upper_brown = np.array([30, 255, 255])  # Yüksek HSV değerleri

# Düz bir kahverengi örneği
brown_color = np.uint8([[[0, 128, 128]]])
hsv_brown = cv2.cvtColor(brown_color, cv2.COLOR_BGR2HSV)
hsv_brown = hsv_brown[0, 0]


print(f"HSV değerleri: {hsv_brown}")

# Belirtilen renk aralığındaki pikselleri maskeleme
mask = cv2.inRange(hsv, lower_brown, upper_brown)

# Maskelenmiş görüntüyü gösterme
cv2.imshow("Mask", mask)

# Maske üzerinde kontur tespiti
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Tomruk olarak kabul edilebilecek konturları çizme ve sayma
log_count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1000:  # Minimum alan sınırı (örnek olarak 1000 piksel)
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        log_count += 1

# Sonuçları gösterme
cv2.imshow("Detected Logs", image)
print(f"Detected logs: {log_count}")

cv2.waitKey(0)
cv2.destroyAllWindows()
