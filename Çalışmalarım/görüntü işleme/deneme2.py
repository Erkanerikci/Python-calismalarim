import torch

# Modeli yükle
model = torch.load('best.pt')
model.eval()

# Dummy input
dummy_input = torch.randn(1, 3, 416, 416)  # Modelin beklediği giriş şekli

# Modeli ONNX formatına çevir
torch.onnx.export(model, dummy_input, "model.onnx")
