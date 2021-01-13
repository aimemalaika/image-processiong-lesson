from PIL import Image,ImageFilter

image = Image.open('./Pokedex/4.5 pikachu.jpg.jpg')

filtered_image = image.filter(ImageFilter.SMOOTH)

filtered_image.save("smooth.png",'png')
#convert image

convert_image = image.convert('L')

convert_image.save('gray.png','png')