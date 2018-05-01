# django_blog
Blog website and get data from mongodb by flask service (restful api)

## Environment
Python Version: 3.6.5<br/>
Deployed Cloud Server: Google App Engine

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
* 支援增刪改查Post
* 支援建立顯示Comment
