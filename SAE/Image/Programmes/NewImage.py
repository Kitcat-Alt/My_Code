from PIL import Image

i = Image.open("SAE/Image/Image3.bmp")
sortie = i.copy()
sortie.save("SAE/Image/Imageout.bmp")