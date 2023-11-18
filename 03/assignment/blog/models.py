from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("account.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, models.CASCADE)
    created_by = models.ForeignKey("account.User", models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_updated = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:30]

class TagPost(models.Model):
    content = models.TextField(max_length=50, primary_key=True)
    post = models.ManyToManyField("Post", related_query_name='tags', related_name='tagPost')

    def __str__(self):
        return self.content

class TagComment(models.Model):
    content = models.TextField(max_length=50, primary_key=True)
    comment = models.ManyToManyField("Comment", related_query_name='tags', related_name='tagComment')

    def __str__(self):
        return self.content