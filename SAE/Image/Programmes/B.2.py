from PIL import Image

coloneInverse = 0

image = Image.open("SAE/Image/images/hall-mod_0.bmp")
image_inverse = image.copy()

def inverse_image(image):
    for ligne in range(image.size[1]):
        for colone in range(image.size[0]):
            coloneInverse = image.size[0]-(colone+1)        
            pixel = image.getpixel((coloneInverse, ligne))
            image_inverse.putpixel((colone, ligne), (pixel))
    return image_inverse.save("SAE/Image/images/Imageout1.bmp")
inverse_image(image)