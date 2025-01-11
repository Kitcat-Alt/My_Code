from PIL import Image

image = Image.open("SAE/Image/images/ImageExemple.bmp")
image_grise = image.copy()
pixel_gray =()

def niveau_de_gris(image):
    for ligne in range(image.size[1]):
        for colone in range(image.size[0]):
            pixel = image.getpixel((colone, ligne))
            pixel_gray = ((pixel[0]+pixel[1]+pixel[2])//3, (pixel[0]+pixel[1]+pixel[2])//3, (pixel[0]+pixel[1]+pixel[2])//3)        
            image_grise.putpixel((colone, ligne), (pixel_gray))
    return image_grise.save("SAE/Image/images/Imageout2.bmp")
niveau_de_gris(image)