from PIL import Image

l0 = Image.open('skilos-2.jpg')
lg = Image.new('L',(l0.size[0],l0.size[1]))
print('size = ',l0.size)
print('pixel[50][50]= ',l0.getpixel((50,50)))
print(max(l0.getpixel((50,50))))
for x in range(l0.size[0]):
    for y in range(l0.size[1]):
        lg.putpixel((x,y),max(l0.getpixel((x,y))))
l0.show()
lg.show()
lg.save('skilos-2_gray.jpg')
