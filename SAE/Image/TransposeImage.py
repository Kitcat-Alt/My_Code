from PIL import Image

i  = Image.open("SAE/Image/ImageTest.bmp")
sortie = i.copy()
for ligne in range(i.size[1]):
    for colone in range(i.size[0]):
        c = i.getpixel((colone, ligne))
        sortie.putpixel((ligne, colone), (c))
sortie.save("SAE/Image/Imageout0.bmp")