from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .httphelp import getPostDetail, patchPostDetail
from .models import Comment
from .forms import CommentForm
import json
from django.views.generic.edit import ProcessFormView

"""
def post_comment(request, post_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    # post = get_object_or_404(Post, pk=post_pk)
    # post = getPostDetail(pk=post_pk)

    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据。
    if request.method == 'POST':
    	post = getPostDetail(pk=post_pk)
    	# 用户提交的数据存在 request.POST 中，这是一个类字典对象。
    	# 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
    	form = CommentForm(request.POST)

    	# 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
    	if form.is_valid():
    		ori_com = form.save(commit=False)
    		str_json = json.dumps(ori_com.to_dict())
    		bytes = str_json.encode('utf-8')
    		post = patchPostDetail(post['pk'], bytes)

    		return redirect('blog:post_detail', pk=post['pk'])
    	else:
			# 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            # 具体请看下面的讲解。
            comment_list = post.get('comments')
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/post_detail.html', context=context)
	# 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect('blog:post_detail', pk=post_pk)
    # return redirect(post)
"""

class PostCommentView(ProcessFormView):
	def post(self, request, *args, **kwargs):
		post = getPostDetail(pk=self.kwargs.get('post_pk'))
		form = CommentForm(request.POST)
		if form.is_valid():
			ori_com = form.save(commit=False)
			str_json = json.dumps(ori_com.to_dict())
			bytes = str_json.encode('utf-8')
			post = patchPostDetail(post['pk'], bytes)
			return redirect('blog:post_detail', pk=post['pk'])
		else:
			comment_list = post.get('comments')
			context =  {'post': post,
						'form': form,
						'comment_list': comment_list
						}
			return render(request, 'blog/post_detail.html', context=context)
	def get(self, request, *args, **kwargs):
		return redirect('blog:post_detail', pk=self.kwargs.get('post_pk'))





