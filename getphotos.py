import vk
import requests
import time
import os
import random
import shutil


def getphotos_by_geo(longt,latt, pid, count = 50, radius = 800):
	vk_token = ''
	vk_session = vk.Session(vk_token)
	vk_api = vk.API(vk_session, v = '5.103')
	if pid!=-1:
		pid = str(pid)
	else:
		pid = str(random.randint(1,1000))
	n = 0

	path = './' + pid + '/'
	os.mkdir('./' + pid)

	photos = vk_api.photos.search(lat = latt, long = longt, count = count, radius = radius)
	for item in photos['items']:

		url = item['sizes'][-1]['url']
		download_photo(path,url,n)
		time.sleep(0.1)

		n += 1

	return path

def delete_photos(path):

	shutil.rmtree(path)


def download_photo(path,url,n):

	f = open(path + str(n) + '.png','wb')
	f.write(requests.get(url).content)
	f.close()

