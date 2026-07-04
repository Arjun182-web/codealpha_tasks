from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(
        blank=True
    )

    profile_pic = models.ImageField(
    upload_to='profiles/',
    blank=True,
    null=True
    )



class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )
    @property
    def total_likes(self):
        return Like.objects.filter(
            post=self
        ).count()


class Like(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="likes"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} liked {self.post.id}"

class Comment(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} commented"

    