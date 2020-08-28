from PIL import Image

im1 = Image.new('L',(300,300))
print(im1.size)
for i in range(im1.size[0]):
	im1.putpixel((i,i),255)
	im1.putpixel((i,im1.size[0]-i-1),255)
im1.show()
