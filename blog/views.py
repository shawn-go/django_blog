from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Tag, Category
from .forms import PostForm
from .httphelp import getPostList, getPostDetail, postPostDetail, putPostDetail, deletePostDetail
import json
from comments.forms import CommentForm

# Create your views here.
def post_list(request):
    # post_list = Post.objects.all().order_by('-created_time')
    post_list = getPostList()
    return render(request, 'blog/post_list.html', context={'post_list': post_list})

def post_detail(request, pk):
    # post = get_object_or_404(Post, pk=pk)
	post = getPostDetail(pk=pk)
	post_ob = Post(title=post['title'], abstract=post['abstract'], body=post['body'], author=post['author'], category=post['category'], pub_time=post['pub_time'], update_time=post['update_time'], pk=post['pk'])

	# 记得在顶部导入 CommentForm
	form = CommentForm()
	# 获取这篇 post 下的全部评论
    # comment_list = post.comment_set.all()
	comment_list = post.get('comments')

	# 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
	context	=	{'post': post,
				'form': form,
				'comment_list': comment_list
				}
	return render(request, 'blog/post_detail.html', context=context)
	# return render(request, 'blog/post_detail.html', context={'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			ori_post = form.save(commit=False)
			str_json = json.dumps(ori_post.to_dict())
			bytes = str_json.encode('utf-8')
			post = postPostDetail(bytes)
			# post = form.save()
			# post.author = request.user
			# post.save()
			# return redirect('blog:post_list')
			return redirect('blog:post_detail', pk=post['pk'])
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	# post = get_object_or_404(Post, pk=pk)
	post = getPostDetail(pk)
	post_ob = Post(title=post['title'], abstract=post['abstract'], body=post['body'], author=post['author'], category=post['category'], pub_time=post['pub_time'], update_time=post['update_time'], pk=post['pk'])
	if request.method == "POST":
		form = PostForm(request.POST, instance=post_ob)
		if form.is_valid():
			ori_post = form.save(commit=False)
			str_json = json.dumps(ori_post.to_dict())
			bytes = str_json.encode('utf-8')
			post = putPostDetail(pk, bytes)
			# post = form.save()
			# post = form.save(commit=False)
			# post.author = request.user
			# post.save()
			return redirect('blog:post_detail', pk=post['pk'])
	else:
		form = PostForm(instance=post_ob)
	return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
	deletePostDetail(pk)
	return redirect('blog:post_list')







