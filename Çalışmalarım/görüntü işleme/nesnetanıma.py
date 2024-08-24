import cv2
import numpy as np

resim = cv2.imread("Griresim.jpg")

resim_width = resim.shape[1]
resim_height = resim.shape[0]

print(resim_width)
print(resim_height)

resim_blob = cv2.dnn.blobFromImage(resim, 1/255, (416, 416), swapRB=True)
labels = ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
          "trafficlight", "firehydrant", "stopsign", "parkingmeter", "bench", "bird", "cat",
          "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
          "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sportsball",
          "kite", "baseballbat", "baseballglove", "skateboard", "surfboard", "tennisracket",
          "bottle", "wineglass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
          "sandwich", "orange", "broccoli", "carrot", "hotdog", "pizza", "donut", "cake", "chair",
          "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
          "remote", "keyboard", "cellphone", "microwave", "oven", "toaster", "sink", "refrigerator",
          "book", "clock", "vase", "scissors", "teddybear", "hairdrier", "toothbrush","tree"]

colors = ["26, 17, 10", "151, 123, 54", "97, 69, 38"]
colors = [np.array(color.split(",")).astype("int") for color in colors]
colors = np.array(colors)
colors = np.tile(colors, (20, 1))

model = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")
layers = model.getLayerNames()

unconnected_out_layers = model.getUnconnectedOutLayers()
print("Unconnected Out Layers:", unconnected_out_layers)
print("Type of Unconnected Out Layers:", type(unconnected_out_layers))

if isinstance(unconnected_out_layers, np.ndarray):
    output_layers = [layers[i - 1] for i in unconnected_out_layers.flatten()]
else:
    output_layers = [layers[unconnected_out_layers - 1]]

print("Output Layers:", output_layers)

model.setInput(resim_blob)

detection_layers = model.forward(output_layers)

for detection_layer in detection_layers:
    for object_detection in detection_layer:
        scores = object_detection[5:]
        predicted_id = np.argmax(scores)
        confidence = scores[predicted_id]

        if confidence > 0.30:
            label = labels[predicted_id]
            bounding_box = object_detection[0:4] * np.array([resim_width, resim_height, resim_width, resim_height])
            (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")

            start_x = int(box_center_x - (box_width / 2))
            start_y = int(box_center_y - (box_height / 2))

            end_x = start_x + box_width
            end_y = start_y + box_height

            box_color = colors[predicted_id]
            box_color = [int(each) for each in box_color]

            cv2.rectangle(resim, (start_x, start_y), (end_x, end_y), box_color, 2)
            cv2.putText(resim, label, (start_x, start_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 1)

cv2.imshow("Tespit Ekranı", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
