from PIL import Image

image = Image.open("SAE/Image/images/IUT-Orleans.bmp")
image_noir_blanc = image.copy()
ValeurMoyenne = (255*255*3)/2

def image_noir_et_blanc(image):
    for ligne in range(image.size[1]):
        for colone in range(image.size[0]):
            pixel = image.getpixel((colone, ligne))
            BlackOrWhite = ((pixel[0]*pixel[0]+pixel[1]*pixel[1]+pixel[2]*pixel[2]))
            if BlackOrWhite > ValeurMoyenne:
                image_noir_blanc.putpixel((colone,ligne), (255,255,255))
            else:
                image_noir_blanc.putpixel((colone,ligne), (0,0,0))
    return image_noir_blanc.save("SAE/Image/images/Imageout3.bmp")
image_noir_et_blanc(image)
