from PIL import Image,ImageFilter

# image = Image.open('./Pokedex/4.5 pikachu.jpg.jpg')

# filtered_image = image.filter(ImageFilter.SMOOTH)

# filtered_image.save("smooth.png",'png')
#convert image

# convert_image = image.convert('L')
# resize = convert_image.resize((30,300))
# resize.save('gray.png','png')

# convert_image = image.convert('L')
# box = (100,100,400,400)
# region = convert_image.crop(box)
# region.save('gray.png','png')


#resizing image

# image = Image.open('./Pokedex/6.1 astro.jpg.jpg')
# newImage =image.thumbnail((400,400))
# newImage.save('thumb.jpg')

image = Image.open('./Pokedex/6.1 astro.jpg.jpg')
image.thumbnail((400,400))
image.save('thumb.jpg')