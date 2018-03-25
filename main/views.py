from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode
from django.db import transaction
from kiteconnect import KiteConnect
import os

from .forms import SignupForm, AddInvestorForm

api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']

# Create your views here.

def index(request):
    ctx = {}
    ctx['access_token'] = request.session.get('access_token', '')
    if ctx['access_token']:
        kite = KiteConnect(api_key=api_key)
        kite.set_access_token(ctx['access_token'])
        ctx['orders'] = kite.instruments()[:10]
    return render(request, "main/index.html", ctx)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.is_agent = False
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})

@login_required
@transaction.atomic
def add_investor(request):
    if request.method == 'POST':
        form = AddInvestorForm(request.POST)
        if request.user.profile.is_agent and form.is_valid():
            form.cleaned_data['password1'] = User.objects.make_random_password()
            form.cleaned_data['password2'] = form.cleaned_data['password1']
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.is_agent = False
            user.profile.referer = request.user
            user.save()
            token = default_token_generator.make_token(user)
            uid = force_text(urlsafe_base64_encode(str(user.pk)))
            return render(request, 'main/added_investor.html', {'token': token, 'uid': uid })
    else:
        form = AddInvestorForm()
    return render(request, 'main/add_investor.html', {'form': form})

@login_required
def profile(request):
    return render(request, "main/profile.html")

def kite_login(request):
    return redirect('https://kite.trade/connect/login?v=3&api_key=%s' % api_key)

def request_token(request):
    token = request.GET.get('request_token')
    kite = KiteConnect(api_key=api_key)
    data = kite.generate_session(token, api_secret)
    request.session['access_token'] = data['access_token']
    return redirect(index)
