from PIL import Image

coloneInverse = 0

i = Image.open("SAE/Image/hall-mod_0.bmp")
sortie = i.copy()

for ligne in range(i.size[1]):
    for colone in range(i.size[0]):
        coloneInverse = i.size[0]-(colone+1)        
        c = i.getpixel((coloneInverse, ligne))
        sortie.putpixel((colone, ligne), (c))
sortie.save("SAE/Image/Imageout1.bmp")
