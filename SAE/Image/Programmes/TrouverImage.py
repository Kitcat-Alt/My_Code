from PIL import Image

def trouver(i):
    return i%2

def cacher(i,b):
    return i-(i%2)+b

i  = Image.open("SAE/Image/Imageout_steg_1.bmp")
trouver_image_cachee = i.copy()

for ligne in range(i.size[1]):
    for colone in range(i.size[0]):
        pixel = i.getpixel((colone, ligne))
        if trouver(pixel[0]) == 0:
            trouver_image_cachee.putpixel((colone, ligne), (255, 255, 255))
        else:
            trouver_image_cachee.putpixel((colone, ligne), (trouver(pixel[0]), 0, 0))
trouver_image_cachee.save("SAE/Image/Imageout3trouve.bmp")
        