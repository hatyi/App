from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.get_username()


class Picture(models.Model):
    file_name = models.CharField(max_length=200)
    image = models.FileField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    visibility = models.SmallIntegerField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def url(self):
        return settings.MEDIA_URL + self.image.name