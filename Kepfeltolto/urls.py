from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^index$', views.home, name='home'),
    url(r'^login$', views.kepfeltolto_login, name='login'),
    url(r'^logout$', views.kepfeltolto_logout, name='logout'),
    url(r'^registration$', views.kepfeltolto_registration, name='registration'),
    url(r'^upload$', views.upload_file, name='upload'),
    url(r'^images$', views.show_images, name='images'),
    url(r'^getusers$', views.get_users, name='get_users'),
    url(r'^addfriend', views.add_friend, name='add_friend'),
    url(r'^getfriends$', views.get_friends, name='get_friends'),
    url(r'^removefriend$', views.remove_friend, name='remove_friend'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)