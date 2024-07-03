from django.shortcuts import render


def home(request):
    return render(request,"home.html")
def account(request):
    return render(request,"account.html")
def groups(request):
    return render(request,"groups.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
