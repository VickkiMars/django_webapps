from django.db import models

# Create your models here.
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profileimg = models.ImageField(upload_to="profile_images", default="blank-profile-picture.png")

    def __str__(self):
        return self.user.username

class Author(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(blank=True)
    # books_published = models.ForeignKey(Book)

    class Meta:
        ordering = ['rating']

    def __str__(self):
        return self.name

class comment(models.Model):
    Comment = models.CharField(max_length=200)
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    no_of_likes = models.IntegerField()

    def __str__(self):
        return self.user

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False)
    pub_date = models.DateField(blank=False)
    rating = models.IntegerField(blank=True)
    views = models.IntegerField(blank=True)
    book = models.FileField(upload_to='books', blank=False)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=False)
    uploaded_by = models.CharField(max_length=100, blank=True)
    time_added = models.DateTimeField(default=datetime.datetime.now)
    category = models.CharField(max_length=100, blank=True)
    comment = models.ManyToManyField(comment, blank=True)
    language = models.CharField(max_length=100, blank=True)
    press = models.CharField(max_length=150, blank=True)
    page_number = models.IntegerField()

    class Meta:
        ordering = ['rating']

    
    def __str__(self):
        return f"{self.author} | {self.title}"

    def was_added_recently(self):
        return self.time_added >= timezone.now() - datetime.timedelta(days=1)



