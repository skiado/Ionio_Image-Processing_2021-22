from PIL import Image
import math

def sigma_f(x):
	return 1 / (1+math.e**(-(10*x - 5)))

im1 = Image.open('labrador_gray.jpg')
im2 = Image.new('L',(im1.size[0],im1.size[1]))
print(im1.size)
for i in range(im1.size[0]):
	for j in range(im1.size[1]):
		s = im1.getpixel((i,j))
		im2.putpixel((i,j),int(s * sigma_f(s/255)))
im1.show()
im2.show()
