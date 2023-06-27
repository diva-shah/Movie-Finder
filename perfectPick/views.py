"""
Copied the layout.html from previous projects because it was in the given distribution code and I did not know how to code it since I did not do it before
For registering users, I copied the try and except code from previous projects since I did not code it before
For the load function, I used lecture 6 for the equation on how to check when to load
Looked up how to delete a sql query in django
"""
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Users, Integer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.
def loginForm(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if not username or not password:
            return render(request, "perfectPick/login.html", {
                "msg" : "Please fill out all fields"
            })
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            print("USER IS NONE")
            return render(request, "perfectPick/login.html", {
                "msg" : "Invalid username/password"
            })
    else:
        return render(request, "perfectPick/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']
        confirm = request.POST['confirm']

        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        if not username or not email or not password or not confirm or not firstName or not lastName:
            return render(request, "perfectPick/register.html", {
                "msg" : "Please fill out all fields",
                "username" : username,
                "email" : email,
                "password" : password,
                "confirm" : confirm,
                "firstName" : firstName,
                "lastName" : lastName
            })
        if password != confirm:
            return render(request, "perfectPick/register.html", {
                "msg" : "Passwords don't match",
                "username" : username,
                "email" : email,
                "firstName" : firstName,
                "lastName" : lastName
            })
        #Got the try and except from previous projects because it was in the given distribution code
        try:
            user = Users.objects.create_user(username, email, password)
            user.save()
            Users.objects.filter(username=username).update(first_name = firstName, last_name=lastName)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            return render(request, "perfectPick/register.html", {
                "msg" : "Username Taken",
                "email" : email,
                "password" : password,
                "confirm" : confirm,
                "firstName" : firstName,
                "lastName" : lastName
            })
    else:
        return render(request, "perfectPick/register.html")

def logoutLink(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required(login_url="/login")
def index(request):
    user = Users.objects.get(id=request.user.id)
    print("index", user.watchlist)
    return render(request, "perfectPick/index.html", {
        "username" : user.username
    })

@login_required(login_url="/login")
def movieInfo(request,movieID):
    try:
        intObject = Integer.objects.get(movieID=movieID)
    except Integer.DoesNotExist:
        add = Integer(movieID=movieID)
        add.save()
    intObject = Integer.objects.get(movieID=movieID)
    watchlist = Users.objects.get(id=request.user.id)
    return render(request, "perfectPick/movieInfo.html", {
        "movieID" : movieID,
        "watchlistM" : watchlist,
        "object" : intObject
    })

@login_required(login_url="/login")
def search(request,category, query):
    return render(request, "perfectPick/search.html", {
        "category" : category,
        "query" : query
    })

@login_required(login_url="/login") 
def watchlistItems(request):
    watchlist = Users.objects.get(id=request.user.id)
    return render(request, "perfectPick/watchlist.html", {
        "items" : watchlist
    })

@login_required(login_url="/login")
def watchlistAdd(request, movieId, removeOrAdd):
    try:
        check = Integer.objects.get(movieID=movieId)
    except Integer.DoesNotExist:
        check = Integer(movieID=movieId)
        check.save()
    identity = Integer.objects.get(movieID=movieId)
    watchlistMovies = get_object_or_404(Users, id=request.user.id)
    if removeOrAdd == 0:
        watchlistMovies.watchlist.add(identity)
    elif removeOrAdd == 1:
        watchlistMovies.watchlist.remove(identity)
    return HttpResponseRedirect(reverse("index"))

@login_required(login_url="/login")
def like(request,movieID,check):
    try:
        check1 = Integer.objects.get(movieID=movieID)
    except Integer.DoesNotExist:
        check1 = Integer(movieID=movieID)
        check1.save()
    objectUser = Users.objects.get(id=request.user.id)
    integer = Integer.objects.get(movieID=movieID)
    if check == 1:
        objectUser.liked.add(integer)
    elif check == 0:
        objectUser.liked.remove(integer)
    intObject = Integer.objects.get(movieID=movieID)
    watchlist = Users.objects.get(id=request.user.id)
    return render(request, "perfectPick/movieInfo.html", {
        "movieID" : movieID,
        "watchlistM" : watchlist,
        "object" : intObject
    })

@login_required(login_url="/login")
def liked(request):
    liked = Users.objects.get(id=request.user.id)
    return render(request, "perfectPick/liked.html", {
        "liked" : liked
    })