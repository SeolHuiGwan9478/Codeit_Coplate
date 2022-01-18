from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters, validate_restaurant_link
class User(AbstractUser):
    nickname = models.CharField(max_length = 15, unique=True, null=True,
        error_messages = {"unique":"이미 사용중인 닉네임입니다."},
        validators=[validate_no_special_characters],
    )

    def __str__(self):
        return self.email
# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=30)
    restaurant_name = models.CharField(max_length=20)
    restaurant_link = models.URLField(validators=[validate_restaurant_link])

    RATING_CHOICES = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES)

    image1 = models.ImageField(upload_to="review_pics")
    image2 = models.ImageField(upload_to="review_pics", blank=True)
    image3 = models.ImageField(upload_to="review_pics", blank=True)
    content = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title