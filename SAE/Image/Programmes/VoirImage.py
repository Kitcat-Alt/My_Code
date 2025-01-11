from PIL import Image

i  = Image.open("SAE/Image/ImageTest.bmp")
for ligne in range(i.size[1]):
    for colone in range(i.size[0]):
        c = i.getpixel((colone, ligne))
        print(c),
    print("")