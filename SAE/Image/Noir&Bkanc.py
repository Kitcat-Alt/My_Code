from PIL import Image

i  = Image.open("SAE/Image/IUT-Orleans.bmp")
sortie = i.copy()
Cgray =()
ValeurMoyenne = (255*255*3)/2

for ligne in range(i.size[1]):
    for colone in range(i.size[0]):
        c = i.getpixel((colone, ligne))
        BlackOrWhite = ((c[0]*c[0]+c[1]*c[1]+c[2]*c[2]))
        if BlackOrWhite > ValeurMoyenne:
            sortie.putpixel((colone,ligne), (255,255,255))
        else:
            sortie.putpixel((colone,ligne), (0,0,0))
sortie.save("SAE/Image/Imageout3.bmp")
