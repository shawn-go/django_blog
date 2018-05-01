from urllib.request import urlopen, Request
import json

def getPostList():
	# url = 'http://0.0.0.0:5000/posts/'
	url = 'https://shorten-url-1491815099304.appspot.com/posts/'
	headers = {'Content-Type': 'application/json'}
	req = Request(url=url, headers=headers)
	res = urlopen(req)
	posts = json.loads(res.read())['posts']
	return posts
	# return res.read()

def getPostDetail(pk):
	# url = 'http://0.0.0.0:5000/posts/{}/'.format(pk)
	url = 'https://shorten-url-1491815099304.appspot.com/posts/{}/'.format(pk)
	headers = {'Content-Type': 'application/json'}
	req = Request(url=url, headers=headers)
	res = urlopen(req)
	post = json.loads(res.read())['post']
	return post

def postPostDetail(data):
	# url = 'http://0.0.0.0:5000/posts/'
	url = 'https://shorten-url-1491815099304.appspot.com/posts/'
	headers = {'Content-Type': 'application/json'}
	req = Request(url=url, headers=headers, data=data)
	res = urlopen(req)
	post = json.loads(res.read())['post']
	return post

def putPostDetail(pk, data):
	# url = 'http://0.0.0.0:5000/posts/{}/'.format(pk)
	url = 'https://shorten-url-1491815099304.appspot.com/posts/{}/'.format(pk)
	headers = {'Content-Type': 'application/json'}
	req = Request(url=url, headers=headers, data=data)
	req.get_method = lambda:'PUT'
	res = urlopen(req)
	post = json.loads(res.read())['post']
	return post

def deletePostDetail(pk):
	# url = 'http://0.0.0.0:5000/posts/{}/'.format(pk)
	url = 'https://shorten-url-1491815099304.appspot.com/posts/{}/'.format(pk)
	headers = {'Content-Type': 'application/json'}
	req = Request(url=url, headers=headers)
	req.get_method = lambda:'DELETE'
	res = urlopen(req)
	# post = json.loads(res.read())['post']
	# return post





