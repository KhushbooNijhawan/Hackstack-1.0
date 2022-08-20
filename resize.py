import PIL
import os
import os.path
from PIL import Image

f = r'image'
for file in os.listdir(f):
    if file.endswith(".DS_Store"):
        continue
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((224,224))
    img.save(f_img)