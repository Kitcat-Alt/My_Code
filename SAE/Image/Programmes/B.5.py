from PIL import Image

def trouver(i):
    return i%2

def cacher(i,b):
    return i-(i%2)+b

#------------------------------------------------------------------------------------------------------

image_base = Image.open("SAE/Image/images/hall-mod_0.bmp")
image_hote = image_base.copy()

def valeur_rouge_pair(image):
    for ligne in range(image.size[1]):
        for colone in range(image.size[0]):
            pixel = image.getpixel((colone, ligne))
            Rouge_pair = pixel[0]-(pixel[0]%2)
            image.putpixel((colone,ligne), (Rouge_pair, pixel[1], pixel[2]))
    return image.save("SAE/Image/images/Imageout_steg_0.bmp")
valeur_rouge_pair(image_hote)

#------------------------------------------------------------------------------------------------------

image_a_cacher = Image.open("SAE/Image/images/Imageout3.bmp")
def cacher_image(image_hote, image_a_cacher):
    for ligne in range(image_a_cacher.size[1]):
        for colone in range(image_a_cacher.size[0]):
                pixel_a_cacher = image_a_cacher.getpixel((colone, ligne))
                pixel_hote = image_hote.getpixel((colone, ligne))
                if pixel_a_cacher == (0,0,0):
                    image_hote.putpixel((colone, ligne),(cacher(pixel_hote[0], 1), pixel_hote[1], pixel_hote[2]))
                else:
                    image_hote.putpixel((colone, ligne), image_hote.getpixel((colone, ligne)))
    return image_hote.save("SAE/Image/images/Imageout_steg_1.bmp")
cacher_image(Image.open("SAE/Image/images/Imageout_steg_0.bmp"), image_a_cacher)

#------------------------------------------------------------------------------------------------------

image_hote = Image.open("SAE/Image/images/Imageout_steg_1.bmp")
image_cachee = image_hote.copy()

def trouver_image(image_hote):
    for ligne in range(image_hote.size[1]):
        for colone in range(image_hote.size[0]):
            pixel = image_hote.getpixel((colone, ligne))
            if trouver(pixel[0]) == 0:
                image_cachee.putpixel((colone, ligne), (255, 255, 255))
            else:
                image_cachee.putpixel((colone, ligne), (0, 0, 0))
    return image_cachee.save("SAE/Image/images/Imageout3trouve.bmp")
trouver_image(image_hote)