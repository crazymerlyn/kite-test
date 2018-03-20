from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def login(request):
    return redirect('https://kite.trade/connect/login?v=3&api_key=hw1kqautubteevkq')

def request_token(request):
    token = request.params['request_token']
    return render(request, 'main/final.html', {'token': token})
