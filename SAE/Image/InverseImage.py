from PIL import Image

coloneInverse = 0
ligneInverse = 0
i  = Image.open("SAE/Image/ImageTest.bmp")
sortie = i.copy()

for ligne in range(i.size[1]):
    ligneInverse += i.size[1]-(ligne+1)
    for colone in range(i.size[0]):
        coloneInverse += i.size[0]-(colone+1)
        c = i.getpixel((coloneInverse, ligneInverse))
        sortie.putpixel((colone, ligne), (c))
        coloneInverse = 0
        ligneInverse -= 1
        if ligneInverse < 0:
            sortie.save("SAE/Image/Imageout1.bmp")
            break
