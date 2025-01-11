from PIL import Image

i = Image.open("SAE/Image/Image0.bmp")
sortie = i.copy()
sortie.putpixel((3,3), (0,0,255))
sortie.save("SAE/Image/Imageout.bmp")