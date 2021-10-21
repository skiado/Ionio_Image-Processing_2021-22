from PIL import Image
import numpy as np

a = np.random.randint(0,255,(256,256),np.uint8)
im1 = Image.fromarray(a)
im1.show()
