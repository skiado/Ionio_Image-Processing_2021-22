from PIL import Image
import numpy as np

l8 = Image.open('lena-gray.jpg')
l8.show()
input()	# Για να σταματήσει η εκτέλεση σ'αυτό το σημείο
l8_array = np.array(l8)  # Μετατροπή εικόνας σε πίνακα
l7_array = np.zeros((l8_array.shape[0]//2,l8_array.shape[1]//2),np.uint8) #νέος πίνακας με 0, μισής διάστασης
for i in range(0,l8_array.shape[0],2):
    for j in range(0,l8_array.shape[1],2):
        l7_array[i//2][j//2] = np.sum(l8_array[i:i+2,j:j+2])//4  #μέσος όρος από (i,j) ως (i+1,j+1)
l7 = Image.fromarray(l7_array)
l7.show()
l7.save('lena-gray_2.jpg')
input()	# Για να σταματήσει η εκτέλεση σ'αυτό το σημείο
l6_array = np.zeros((l7_array.shape[0]//2,l7_array.shape[1]//2),np.uint8)
for i in range(0,l7_array.shape[0],2):
    for j in range(0,l7_array.shape[1],2):
        l6_array[i//2][j//2] = np.sum(l7_array[i:i+2,j:j+2])//4
l6 = Image.fromarray(l6_array)
l6.show()
l6.save('lena-gray_4.jpg')
input()	# Για να σταματήσει η εκτέλεση σ'αυτό το σημείο
l5_array = np.zeros((l6_array.shape[0]//2,l6_array.shape[1]//2),np.uint8)
for i in range(0,l6_array.shape[0],2):
    for j in range(0,l6_array.shape[1],2):
        l5_array[i//2][j//2] = np.sum(l6_array[i:i+2,j:j+2])//4
l5 = Image.fromarray(l5_array)
l5.show()
l5.save('lena-gray_8.jpg')
