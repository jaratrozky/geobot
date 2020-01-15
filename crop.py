from PIL import Image
import face_recognition
from IPython.display import display
import os
import io
import numpy as np
from math import degrees as dg
# for i in range(45):
# 	image = face_recognition.load_image_file('./1/'+str(i)+'.png')
# 	face_locations = face_recognition.face_locations(image)
# 	print(face_locations)
def crop(path):
	x = 0
	os.mkdir(path+'cropped')
	for i in range(len(os.listdir(path)) - 1):
		# x = 0
		img = Image.open(path + str(i) + '.png')
		image = face_recognition.load_image_file(path + str(i) + '.png')
		face_locations = face_recognition.face_locations(image)
		marks = face_recognition.face_landmarks(image)
		# if face_locations != []:
		# 	os.mkdir(path + str(i) + '/')
		if len(face_locations) != 1:
			for j in face_locations:

				temp = (j[3], j[0], j[1], j[2])
				img2 = img.crop(temp)

				for z in marks:
					img2 = rotate(z, img2, j)

				img2.save(path + 'cropped/' + str(x) + '.png')
				x += 1

		elif len(face_locations) != 0 and len(marks) != 0:
			z = marks[0]
			j = face_locations[0]
			img2 = rotate(z, img, j)

			imgByteArr = io.BytesIO()
			img2.save(imgByteArr, format='PNG')
			kek = face_recognition.load_image_file(imgByteArr)
			try:
				j = face_recognition.face_locations(kek)[0]
				temp = (j[3], j[0], j[1], j[2])
				img2 = img2.crop(temp)
				img2.save(path + 'cropped/' + str(x) + '.png')
			except:
				pass
			x += 1

def rotate(marks, face, j ):
	left = marks['left_eye']
	right = marks['right_eye']

	lc = ((left[0][0]+left[3][0])//2,(left[0][1]+left[3][1])//2)
	rc = ((right[0][0]+right[3][0])//2,(right[0][1]+right[3][1])//2)
	if lc[0] > j[3] and lc[0] < j[1] and lc[1] < j[2] and lc[1] > j[0]:
	# if True:
		x = rc[0] - lc[0]
		y = lc[1] - rc[1]
		z = np.sqrt(x ** 2 + y ** 2)
		alpha = dg(np.arccos(x/z))
		if alpha > 5:
			if y < 0	:
				face = face.rotate(alpha)
			else:
				face = face.rotate(-1 * alpha)
	return face
