import os

def aver(path):
	os.system('python3 face_morpher-dlib/facemorpher/averager.py --images='+path+' --out='+ path + 'aver.png')