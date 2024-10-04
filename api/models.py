from django.contrib.auth.models import User
from django.db import models


class Chirp(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.text


class Relationship(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.follower} follows {self.following}"


class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chirp_id = models.ForeignKey(Chirp, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user_id} liked {self.chirp_id} at {self.timestamp}"
