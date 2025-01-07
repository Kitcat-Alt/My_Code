from PIL import Image

def trouver(i):
    return i%2

def cacher(i,b):
    return i-(i%2)+b

i  = Image.open("SAE/Image/Imageout_steg_1.bmp")
sortie_image_cachee = i.copy()

for ligne in range(i.size[1]):
    for colone in range(i.size[0]):
        c = i.getpixel((colone, ligne))
        if trouver()
        