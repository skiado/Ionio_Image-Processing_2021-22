from PIL import Image

im1 = Image.new('L',(256,256))
print(im1.size)
for i in range(im1.size[0]):
	for j in range(im1.size[1]):
		im1.putpixel((i,j),i)
im1.show()
im3 = Image.open('lena-gray.jpg')
im3.show()
im_add = Image.new('L',(256,256))
im_sub = Image.new('L',(256,256))
for i in range(im_add.size[0]):
	for j in range(im_add.size[1]):
		inten = im1.getpixel((i,j)) + im3.getpixel((i,j))
		if inten > 255:
			inten = 255
		im_add.putpixel((i,j),inten)
		inten = im3.getpixel((i,j)) - im1.getpixel((i,j))
		if inten < 0:
			inten = 0
		im_sub.putpixel((i,j),inten)
im_add.show()
im_sub.show()
