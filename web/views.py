from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest,HttpResponseRedirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import User, Note
from uuid import uuid4

def homepage(request, token):
    #showing latest downloads
    user = User.objects.filter(token=token).get()
    if user.signedin == 'True':
        files = Note.objects.all()
        context = {
            'files': files,
            'user': user
        }
        return render(request, "homepage.html", context)
    else:
        return redirect('/signin/')


@csrf_exempt

def signup_attempt(request):
    if User.objects.filter(useremail=request.POST['email']).exists():
        errormessage = {"error":"A user already exists with the given email"}
        return render(request, "signuppage.html", errormessage)
    elif User.objects.filter(username=request.POST['user']).exists():
        errormessage = {"error":"Username already exists"}
        return render(request, "signuppage.html", errormessage)
    else:
        newuser = User.objects.create(first_name=request.POST["fname"], last_name=request.POST["lname"],useremail=request.POST["email"], username=request.POST["user"],password=request.POST["passw"], token=uuid4(), signedin= 'True')
        newuser.save()
        return redirect('/home/' + str(newuser.token))


def signin_attempt(request):
    if User.objects.filter(username=request.POST['user']).exists():
        newuser = User.objects.filter(username=request.POST['user']).get()
        if request.POST['passw'] == newuser.password:
            newuser.signin()
            newuser.save()
            print(newuser.signedin)
            return redirect('/home/'+newuser.token)
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
    if User.signedin == 'True':
        user = User.objects.filter(username=request.POST['user']).get()
        Note.objects.create(link=request.FILES.get('file'), describtion =request.POST['desc'], username=user, name=request.POST['name'], prof='shit')
        return redirect('/home/' + user.token)
    else:
        render(request, "signinpage.html")

def signout(request, token):
    user = User.objects.filter(token=token).get()
    user.signout()
    user.save()
    return redirect('/signin/')
