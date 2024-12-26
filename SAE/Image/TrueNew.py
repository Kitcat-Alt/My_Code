from PIL import Image

i = Image.open("SAE/Image/Image0.bmp")
sortie = Image.new(i.mode, i.size)
sortie.putdata(i.getdata())
sortie.save("SAE/Image/Imageout.bmp")