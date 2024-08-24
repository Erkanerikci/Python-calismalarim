import cv2
import numpy as np

# Maskelenmiş görüntüyü yükleme
mask = cv2.imread('T.jpg', cv2.IMREAD_GRAYSCALE)

# Maskelenmiş bölgedeki beyaz bölgelerin konturlarını bulma
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Beyaz dairelerin sayısını ve çaplarını bulma
white_circle_count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1000:  # Minimum alan sınırı (örnek olarak 1000 piksel)
        # En küçük kapsayan daireyi hesaplama
        (x, y), radius = cv2.minEnclosingCircle(contour)
        diameter = int(2 * radius)
        
        # Beyaz daireyi çizme
        cv2.circle(mask, (int(x), int(y)), int(radius), (255), 2)
        
        # Beyaz daire sayısını ve çapını ekrana yazdırma
        print(f"Detected white circle - Center: ({int(x)}, {int(y)}), Radius: {int(radius)}")
        
        # Beyaz daire sayısını artırma
        white_circle_count += 1

# Sonuçları gösterme
cv2.imshow("Masked White Circles", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bulunan maskelenmiş beyaz daire sayısını ekrana yazdırma
print(f"Detected masked white circles: {white_circle_count}")
