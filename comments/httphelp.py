from urllib.request import urlopen, Request
import json

def getPostDetail(pk):
	# url = 'http://0.0.0.0:5000/posts/{}/'.format(pk)
	url = 'https://shorten-url-1491815099304.appspot.com/posts/{}/'.format(pk)
	headers = {'Content-Type': 'application/json'}
	req = Request(url=url, headers=headers)
	res = urlopen(req)
	post = json.loads(res.read())['post']
	return post

def patchPostDetail(pk, data):
	# url = 'http://0.0.0.0:5000/posts/{}/'.format(pk)
	url = 'https://shorten-url-1491815099304.appspot.com/posts/{}/'.format(pk)
	headers = {'Content-Type': 'application/json'}
	req = Request(url=url, headers=headers, data=data)
	req.get_method = lambda:'PATCH'
	res = urlopen(req)
	post = json.loads(res.read())['post']
	return post

