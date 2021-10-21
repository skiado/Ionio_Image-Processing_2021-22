from PIL import Image

im1 = Image.open('lena-gray_4.jpg')
im1.show()
input() # Για να σταματήσει η εκτέλεση σ'αυτό το σημείο
im2 = Image.new('L',(im1.size[0]*8,im1.size[1]*8))
for i in range(im2.size[0]):
    for j in range(im2.size[1]):
        im2.putpixel((i,j),im1.getpixel((i//8,j//8)))
im2.show()
