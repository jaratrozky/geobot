import numpy as np
from PIL import Image
import os
def check_len(path):
	mas = []
	for i in os.listdir(path):
		f = Image.open(path + i)
		temp = np.array(f)

		if len(temp) >= 128:
			f = f.resize((128,128))
			f.save(path + i)
			f.close()
			mas.append(temp)
		else:
			f.close()
			os.remove(path + i)