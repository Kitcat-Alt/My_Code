from PIL import Image

def cacher(i,b):
    return i-(i%2)+b       

i2 = Image.open("SAE/Image/Imageout3.bmp")
image_hote = Image.open("SAE/Image/hall-mod-pixels-rouges.bmp")
for ligne in range(i2.size[1]):
    for colone in range(i2.size[0]):
            c2 = i2.getpixel((colone, ligne))
            c3 = image_hote.getpixel((colone, ligne))
            if c2[0] == 0 and c2[1] == 0 and c2[2] == 0:
                image_hote.putpixel((colone, ligne),(cacher(c3[0], 1), c3[1], c3[2]))
            else:
                image_hote.putpixel((colone, ligne), image_hote.getpixel((colone, ligne)))
image_hote.save("SAE/Image/Imageout_steg_1.bmp")