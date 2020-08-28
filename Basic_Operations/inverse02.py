from PIL import Image

def inverse_image(im):
	im1 = im.copy()
	for i in range(im1.size[0]):
		for j in range(im1.size[1]):
			im1.putpixel((i,j),255-im1.getpixel((i,j)))
	return im1

im3 = Image.open('lena-gray.jpg')
print(im3.size)
im3.show()
inverse_image(im3).show()
