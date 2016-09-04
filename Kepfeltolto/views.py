from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from .forms import UploadFileForm, FileForm
from .models import Picture, Profile
from .moduls import handle_uploaded_file, create_profile


@login_required
def home(request, fasz = None):
    return render(request, "Kepfeltolto/home.html", {
        "username": request.user.username
    })


def kepfeltolto_login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)

            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(redirect_to='/home')
            else:
                return render(request, "Kepfeltolto/login.html", {
                    "msg": "Nem létező felhasználói adatok."
                })
        else:
            return render(request, "Kepfeltolto/login.html", {
                "msg": "Írd be a bejelentkezési adataid."
            })
    else:
        return HttpResponseRedirect(redirect_to='/home')


def kepfeltolto_registration(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            username = request.POST.get("username")
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                create_profile(username, request.POST.get("password"))
                return render(request, "Kepfeltolto/home.html", {
                    "msg": "Gratulálok sikeresen regisztráltál",
                    "username": username
                })

        return render(request, "Kepfeltolto/registration.html")
    else:
        return HttpResponseRedirect(redirect_to='/home')

@login_required
def kepfeltolto_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request)
            return HttpResponseRedirect('/home')
    else:
        form = FileForm()
    return render(request, 'Kepfeltolto/image_upload.html', {'form': form})


@login_required
def show_images(request):
    imageset = Picture.objects.filter(owner=request.user.profile)
    return render(request, "Kepfeltolto/images.html", {
        "imageset":imageset
    })

@login_required
def get_users(request):
    users = [user for user in User.objects.all().values('id', 'username')]
    return JsonResponse(users, safe=False)


@login_required
def add_friend(request):
    if request.method == 'GET':
        id = request.GET.get("id", "")
        if id is not None:
            target_profile = User.objects.get(pk=id).profile
            request.user.profile.friends.add(target_profile)
            return HttpResponseRedirect("/home")
    else:
        return HttpResponseRedirect("/home")


@login_required
def get_friends(request):
    #friendset = [profile for profile in request.user.profile.friends.all().values()]
    #friends = dict(name=profile.user.username for profile in request.user.profile.friends.all())
    friends = []
    for profile in request.user.profile.friends.all():
        friends.append({"name": profile.user.username, "id": profile.user.id})
    return JsonResponse(friends, safe=False)

@login_required
def remove_friend(request):
    if request.method == 'GET':
        id = request.GET.get("id", "")
        if id is not None:
            try:
                target_profile = User.objects.get(pk=id).profile
            except User.DoesNotExist:
                return HttpResponseRedirect("/home")
            request.user.profile.friends.remove(target_profile)
            return HttpResponseRedirect("/home")
    else:
        return HttpResponseRedirect("/home")