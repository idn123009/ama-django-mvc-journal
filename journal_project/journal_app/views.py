from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Entry
from .forms import EntryForm

# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User is invalid or does not exist')
            
    context = {'page':page}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            for field in form:
                if(field.errors):
                    messages.error(request, 'An error occured during registration:')
                    for error in field.errors:
                        messages.error(request, error)
                        
    context = {'page':page, 'form':form}
    return render(request, 'login_register.html', context)

@login_required(login_url="login")
def home(request):
    entries = Entry.objects.filter(user=request.user)
    context = {'entries':entries}
    return render(request, 'home.html', context)

@login_required(login_url="login")
def entry(request, pk):
    entry = Entry.objects.get(id=pk)
    context = {'entry': entry}
    return render(request, 'entry.html', context)

@login_required(login_url="login")
def createEntry(request):
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'entry_form.html', context)

@login_required(login_url="login")
def updateEntry(request, pk):
    entry = Entry.objects.get(id=pk)
    form = EntryForm(instance=entry)
    
    if request.user != entry.user:
        return HttpResponse("Not Found")
    
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    
    context = {'form':form}
    return render(request, 'entry_form.html', context)

@login_required(login_url="login")
def deleteEntry(request, pk):
    entry = Entry.objects.get(id=pk)
    
    if request.user != entry.user:
        return HttpResponse("Not Found")
    
    if request.method == 'POST':
        entry.delete()
        return redirect('home')
    return render(request, 'delete.html',{'obj':entry})