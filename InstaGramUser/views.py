from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from InstaGramUser.models import InstaGramUser
from InstaGramUser.forms import LoginForm, SignupForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get("password"))
            if user:
                login(request, user)
                # return render(request, 'index.html', {"form": form})
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request, 'base.html', {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                displayname=data.get("displayname")
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'base.html', {"form": form})