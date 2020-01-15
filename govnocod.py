import getphotos
from crop import crop
from check_len import check_len
from aver import aver

def govnocod(coords,pid = -1):
	path = getphotos.getphotos_by_geo(coords[0],coords[1], pid)
	crop(path)
	path_c = path + 'cropped/'
	check_len(path_c)
	aver(path_c)
	return path_c + 'aver.png'