# django_blog
Blog website and get data from mongodb by flask service (restful api)

## Environment
Python Version: 3.6.5<br/>
Django version: 2.0.4<br/>
Deployment: GAE (Google App Engine)

## Models
* Post
  * Title
  * Abstract(optional)
  * Body(內文)
  * Author
  * Category(optional)
  * pub_time(發佈日期;auto)
  * update_time(修改日期;auto)
* Comment
  * name(default='Anonymous';匿名評論)
  * email
  * url(optional)
  * text(評論內容)
  * created_time(評論時間;auto)

## Class-Based Views
* Support CRUD for post(s) -> PostView(ListView), PostDetailView(DetailView), PostNewView(FormView), PostEditView(FormView), PostDeleteView(RedirectView)
* Support CR for comment(s) -> PostCommentView(ProcessFormView)

## Access mongodb through flask service restful api
* httphelp.py
