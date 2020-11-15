# name all jpg images sequentially
import os
from PIL import Image

path = '/Users/victo/Documents/capstone/Pi-Ai/app/learningImages/dandelions/train'
files = os.listdir(path)
last_file = 0

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
    last_file = index

# convert jpgs to png's
for i in range(last_file):
    im = Image.open('train/{}.jpg'.format(i))
    im.save('train/{}.png'.format(i))
    os.remove('train/{}.jpg'.format(i))