from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth import authenticate

def index(request):
    return render( request, 'index.html', {
        'message': 'product list',
        'title': 'products',
        'products': [
            {'title':'playera', 'price': 5, 'stock':True},
            {'title':'camisa', 'price': 7, 'stock':True},
            {'title':'Mochila', 'price': 20, 'stock':False},
            {'title':'Laptop', 'price': 500, 'stock':True},
        ]
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            print("Usuario autenticato")
        else:
            print("Usuario no autenticado")

    return render( request, 'users/login.html', {

    })