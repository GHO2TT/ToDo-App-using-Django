from django.shortcuts import render, redirect
from .forms import twoDoForm
from django.contrib.auth.decorators import login_required
from .models import twoDo

# Create your views here.


@login_required
def index(request):
    twodo = twoDo.objects.filter(author=request.user)

    if request.method == "POST":
        form = twoDoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("index")
    else:
        form = twoDoForm()

    context = {
        "form": form,
        "twodo": twodo,
    }

    return render(request, "list/index.html", context)

@login_required
def delete(request, pk):
    twodo = twoDo.objects.get(author=request.user, id=pk)
    twodo.delete()
    return redirect("index")

@login_required
def update(request, pk):
    twodo = twoDo.objects.get(author=request.user, id=pk)
    if twodo.complete == True:
        twodo.complete = False
        twodo.save()
    else:
        twodo.complete = True
        twodo.save()
    return redirect("index")
