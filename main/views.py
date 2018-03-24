from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from kiteconnect import KiteConnect
import os

api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']

# Create your views here.

@login_required
def index(request):
    ctx = {}
    ctx['access_token'] = request.session.get('access_token', '')
    if ctx['access_token']:
        kite = KiteConnect(api_key=api_key)
        kite.set_access_token(ctx['access_token'])
        ctx['orders'] = kite.instruments()[:10]
    return render(request, "main/index.html", ctx)

def login(request):
    return redirect('https://kite.trade/connect/login?v=3&api_key=%s' % api_key)

def request_token(request):
    token = request.GET.get('request_token')
    kite = KiteConnect(api_key=api_key)
    data = kite.generate_session(token, api_secret)
    request.session['access_token'] = data['access_token']
    return redirect(index)
