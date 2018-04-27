from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
	url(r'^$', views.PostView.as_view(), name='post_list'),
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\w+)/$', views.PostDetailView.as_view(), name='post_detail'),
    # url(r'^post/(?P<pk>\w+)/$', views.post_detail, name='post_detail'),
    url(r'^postnew/$', views.PostNewView.as_view(), name='post_new'),
    # url(r'^postnew/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\w+)/edit/$', views.PostEditView.as_view(), name='post_edit'),
	# url(r'^post/(?P<pk>\w+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\w+)/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
	# url(r'^post/(?P<pk>\w+)/delete/$', views.post_delete, name='post_delete'),
]
