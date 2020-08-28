from PIL import Image

im1 = Image.new('L',(256,256))
print(im1.size)
for i in range(im1.size[0]):
	for j in range(im1.size[1]):
		im1.putpixel((i,j),i)
im1.show()
