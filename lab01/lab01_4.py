from PIL import Image
import numpy as np

im1 = Image.open('parrot.png')
a = np.array(im1)
print(a)
im1.show()
print(im1.size)

for i in range(im1.size[0]):
    for j in range(im1.size[1]):
        im1.putpixel((i,j),255-im1.getpixel((i,j)))
im1.show()
