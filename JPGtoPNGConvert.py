import sys
import os
from PIL import Image

#grab arguments

origin_folder = sys.argv[1]
destination_folder = sys.argv[2]

# check if new folder exist
if not os.path.exists(destination_folder) : os.makedirs(destination_folder)

# loop into the Pokedx folder and convert into png

for filename in os.listdir(origin_folder):
    image = Image.open(f'{origin_folder}{filename}')
    #convert images
    image_name = os.path.splitext(filename)[0]
    print(image_name)
    image.save(f'{destination_folder}{image_name}.png','png')
    print('converted !')
# save into the new folder