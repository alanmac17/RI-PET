from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Dog"), (1, "Cat"), (2, "Bird"), (3, "Fish"), (4, "Small Mammal/rodent"), (5, "Reptile/amphibian"), (6, "Farm Animal"))


class DeathNotice(models.Model):
    title = models.CharField(max_length=200, unique=True)
    posted = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    deceased_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    death_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-death_date"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    deathnotice = models.ForeignKey(DeathNotice, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
