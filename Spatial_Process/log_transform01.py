from PIL import Image
import math

def log_f(x,c):
	return c * math.log(1+x) 

im1 = Image.open('labrador_gray.jpg')
im2 = Image.new('L',(im1.size[0],im1.size[1]))
c = 10
for i in range(im1.size[0]):
	for j in range(im1.size[1]):
		s = im1.getpixel((i,j))
		im2.putpixel((i,j),int(log_f(s,c)))
im1.show()
im2.show()
im2.save('labrador_gray_log.jpg')
