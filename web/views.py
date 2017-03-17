from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest,HttpResponseRedirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import User, Note


def homepage(request, user):
    #showing latest downloads
    files = Note.objects.all()
    context = {
        'files': files,
        'user': user
    }
    return render(request, "homepage.html", context)


@csrf_exempt

def signup_attempt(request):
    if User.objects.filter(useremail=request.POST['email']).exists():
        errormessage = {"error":"A user already exists with the given email"}
        return render(request, "signuppage.html", errormessage)
    elif User.objects.filter(username=request.POST['user']).exists():
        errormessage = {"error":"Username already exists"}
        return render(request, "signuppage.html", errormessage)
    else:
        newuser = User.objects.create(first_name=request.POST["fname"], last_name=request.POST["lname"],useremail=request.POST["email"], username=request.POST["user"],password=request.POST["passw"])
        newuser.save()
        return homepage(request, newuser.username)


def signin_attempt(request):
    if User.objects.filter(username=request.POST['user']).exists():
        newuser = User.objects.filter(username=request.POST['user']).get()
        if request.POST['passw'] == newuser.password:
            return homepage(request, newuser.username)
        else:
            errormessage = {"error": "Your Password is incorrect"}
            return render(request, "signinpage.html", errormessage)
    else:
        errormessage = {"error": "Your Username is incorrect"}
        return render(request, "signinpage.html", errormessage)


def signinpage(request):
    return render(request, "signinpage.html")


def signuppage(request):
    return render(request, "signuppage.html")


def upload(request):
    newfile = Note.objects.create(link=request.FILES.get('file'), describtion =request.POST['desc'], username=User.objects.filter(username=request.POST['user']).get(), name=request.POST['name'])
    return homepage(request, newfile.username)

