import os

# Dosyaların bulunduğu dizin
directory = r'D:\İndirilenler\Yeni klasör'

files = os.listdir(directory)

for filename in files:
    if '.exe' in filename:
        continue
    
    old_path = os.path.join(directory, filename)

    new_filename = filename[2:]
    
    new_path = os.path.join(directory, new_filename)
    
    os.rename(old_path, new_path)

print("Dosya isimleri başarıyla değiştirildi.")
