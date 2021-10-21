from PIL import Image
import numpy as np

a = np.zeros((256,256),np.uint8)
im1 = Image.fromarray(a)
im1.show()

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        a[i][j] = i
im1 = Image.fromarray(a)
im1.show()

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        a[i][j] = j
im1 = Image.fromarray(a)
im1.show()
