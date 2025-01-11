from PIL import Image

image  = Image.open("SAE/Image/images/ImageTest.bmp")
image_transpose = image.copy()

def transpose_image(image):
    for ligne in range(image_transpose.size[1]):
        for colone in range(image_transpose.size[0]):
            pixel = image.getpixel((colone, ligne))
            image_transpose.putpixel((ligne, colone), (pixel))
    return image_transpose.save("SAE/Image/images/Imageout0.bmp")
transpose_image(image)