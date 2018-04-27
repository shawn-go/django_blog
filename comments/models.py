from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100, default='Anonymous')
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    # post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    # post_id = models.CharField(max_length=50)

    def to_dict(self):
        post_dict = {}
        post_dict['name'] = self.name
        post_dict['email'] = self.email
        post_dict['url'] = self.url
        post_dict['text'] = self.text
        # post_dict['created_time'] = self.created_time
        return post_dict

    def __str__(self):
        return self.text[:20]