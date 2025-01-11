from PIL import Image

i  = Image.open("SAE/Image/ImageExemple.bmp")
sortie = i.copy()
Cgray =()

for ligne in range(i.size[1]):
    for colone in range(i.size[0]):
        c = i.getpixel((colone, ligne))
        Cgray = ((c[0]+c[1]+c[2])//3, (c[0]+c[1]+c[2])//3, (c[0]+c[1]+c[2])//3)        
        sortie.putpixel((colone, ligne), (Cgray))
sortie.save("SAE/Image/Imageout2.bmp")