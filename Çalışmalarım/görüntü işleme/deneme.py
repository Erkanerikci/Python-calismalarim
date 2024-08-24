import torch
import cv2
import numpy as np

# Modeli ve ağırlıkları yükleyin
model = torch.load("best.pt")
model.eval()  # Modeli değerlendirme moduna alın

# Etiketleri tanımlayın
labels = ["label1", "label2", "label3"]  # Kendi etiketlerinizi buraya ekleyin
colors = np.random.uniform(0, 255, size=(len(labels), 3))

# Görüntüyü yükleyin ve boyutlarını alın
resim = cv2.imread("Griresim.jpg")
resim_height, resim_width = resim.shape[:2]

# Görüntüyü blob formatına dönüştür ve PyTorch tensor'üne dönüştür
resim_blob = cv2.resize(resim, (416, 416))
resim_blob = np.transpose(resim_blob, (2, 0, 1))  # (H, W, C) -> (C, H, W)
resim_blob = np.expand_dims(resim_blob, axis=0)  # (C, H, W) -> (1, C, H, W)
resim_blob = torch.from_numpy(resim_blob).float() / 255.0

# Modeli çalıştır
with torch.no_grad():
    detections = model(resim_blob)[0]

# Nesne tespiti ve kutuları çizme
for detection in detections:
    if detection['scores'] > 0.3:  # Güven eşiği
        box = detection['boxes']
        class_id = detection['labels'].item()
        confidence = detection['scores'].item()

        x1, y1, x2, y2 = box.tolist()
        color = [int(c) for c in colors[class_id]]
        cv2.rectangle(resim, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        text = f"{labels[class_id]}: {confidence:.2f}"
        cv2.putText(resim, text, (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Sonuçları göster
cv2.imshow("Tespit Ekranı", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
