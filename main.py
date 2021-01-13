from PIL import Image,ImageFilter

image = Image.open('./Pokedex/4.5 pikachu.jpg.jpg')

# filtered_image = image.filter(ImageFilter.SMOOTH)

# filtered_image.save("smooth.png",'png')
#convert image

# convert_image = image.convert('L')
# resize = convert_image.resize((30,300))
# resize.save('gray.png','png')

convert_image = image.convert('L')
box = (100,100,400,400)
region = convert_image.crop(box)
regiongit .save('gray.png','png')
