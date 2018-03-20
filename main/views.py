from django.shortcuts import render, redirect
import os

api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def login(request):
    return redirect('https://kite.trade/connect/login?v=3&api_key=%s' % api_key)

def request_token(request):
    token = request.params['request_token']
    return render(request, 'main/final.html', {'token': token})
