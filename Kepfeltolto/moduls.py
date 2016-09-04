import os
from django.conf import settings
from .models import Picture, Profile
from django.contrib.auth.models import User

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def handle_uploaded_file(req):
    instance = Picture()
    image = req.FILES['image']
    profile = req.user.profile
    instance.file_name = image.name
    instance.image = image
    instance.owner = profile
    instance.visibility = 1
    instance.save()


def create_profile(username, password):
    new_profile = Profile()
    new_profile.user = User.objects.create_user(username=username, password=password)
    new_profile.username = username
    # new_profile.user.is_staff = True
    new_profile.save()