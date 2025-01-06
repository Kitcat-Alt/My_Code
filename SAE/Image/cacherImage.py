from PIL import Image

def cacher(i,b):
    return i-(i%2)+b

i  = Image.open("SAE/Image/hall-mod_0.bmp")
sortie_pixel_rouges = i.copy()

for ligne in range(i.size[1]):
    for colone in range(i.size[0]):
        c = i.getpixel((colone, ligne))
        R = c[0]-(c[0]%2)
        sortie_pixel_rouges.putpixel((colone,ligne), (R, c[1], c[2]))
sortie_pixel_rouges.save("SAE/Image/hall-mod-pixels-rouges.bmp")            

i2 = Image.open("SAE/Image/Imageout3.bmp")
sortie_image_cachee = sortie_pixel_rouges.copy()
for ligne in range(i.size[1]):
    for colone in range(i.size[0]):
        if ligne <= i2.size[1] and colone <= i2.size[0]:
            c2 = i2.getpixel((colone, ligne))
            sortie_image_cachee.putpixel((colone, ligne),(cacher(c[0], 0), c[1], c[2]))
sortie_image_cachee.save("SAE/Image/Imageout_steg_1.bmp")