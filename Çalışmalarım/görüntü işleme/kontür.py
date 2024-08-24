import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('T.jpg')

# Görüntüyü HSV renk uzayına dönüştürme
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Kahverengi renk aralığını tanımlama (örnek aralık)
lower_brown = np.array([10, 50, 50])    # Düşük HSV değerleri
upper_brown = np.array([30, 255, 255])  # Yüksek HSV değerleri

# Belirtilen renk aralığındaki pikselleri maskeleme
mask = cv2.inRange(hsv, lower_brown, upper_brown)

# Maskelenmiş bölgede beyaz bölgelerin konturlarını bulma
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Maskelenmiş bölgedeki beyaz dairelerin sayısını ve çaplarını bulma
white_circle_count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1000:  # Minimum alan sınırı (örnek olarak 1000 piksel)
        # En küçük kapsayan daireyi hesaplama
        (x, y), radius = cv2.minEnclosingCircle(contour)
        diameter = int(2 * radius)
        
        # Maske uygulanan bölgede beyaz daireyi çizme
        cv2.circle(mask, (int(x), int(y)), int(radius), (255), 2)
        
        # Beyaz daire sayısını ve çapını ekrana yazdırma
        print(f"Detected white circle - Center: ({int(x)}, {int(y)}), Radius: {int(radius)}")
        
        # Beyaz daire sayısını artırma
        white_circle_count += 1

# Sonuçları gösterme
cv2.imshow("Masked White Circles", mask)
cv2.imwrite("Maskeli.jpg",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bulunan maskelenmiş beyaz daire sayısını ekrana yazdırma
print(f"Detected masked white circles: {white_circle_count}")
