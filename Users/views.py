from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm




# Create your views here.

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # .is_valid checks to see if the user input is following the
            # the rules and properties of the form
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()

    context = {
        "form" : form,
    }
    return render(request, "users/signup.html", context)



