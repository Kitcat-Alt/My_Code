from PIL import Image
i  = Image.open("SAE/Image/hall-mod_0.bmp")
sortie_pixel_rouges = i.copy()

for ligne in range(i.size[1]):
    for colone in range(i.size[0]):
        c = i.getpixel((colone, ligne))
        R = c[0]-(c[0]%2)
        sortie_pixel_rouges.putpixel((colone,ligne), (R, c[1], c[2]))
sortie_pixel_rouges.save("SAE/Image/hall-mod-pixels-rouges.bmp")