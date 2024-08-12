from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *

# Create your views here.
Buyer = ["Alice", "bob", "Charlie"]

def handle_registration(form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    repeat_password = form.cleaned_data['repeat_password']
    age = form.cleaned_data['age']

    if password != repeat_password:
        return {'error': "Пароли не совпадают", 'form': form}
    elif age < 18:
        return {'error': "Вы должны быть старше 18", 'form': form}
    elif username in Buyer:
        return {'error': "Пользователь уже существует", 'form': form}
    else:
        Buyer.append(username)
        return {'message': f"Приветствуем, {username}!", 'form': UserRegister()}
    if password == repeat_password and int(age) >= 18 and username not in buyers:
        Buyer.objects.create(name=username, balance=balance, age=age)
        return HttpResponse(f"Приветствуем, {username}!")



def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        try:
            age = int(age)
        except ValueError:
            age = None

        if password != repeat_password:
            info = {'error': 'Пароли не совпадают', 'form': UserRegister(request.POST)}
        elif age is None or age < 18:
            info = {'error': 'Вы должны быть старше 18', 'form': UserRegister(request.POST)}
        elif username in Buyer:
            info = {'error': 'Пользователь уже существует', 'form': UserRegister(request.POST)}
        else:
            Buyer.append(username)
            info = {'message': f"Приветствуем, {username}!", 'form': UserRegister()}
        return render(request, 'registration_page.html', info)
    return render(request, 'registration_page.html', {'form': UserRegister()})
    if password == repeat_password and int(age) >= 18 and username not in buyers:
        Buyer.objects.create(name=username, balance=balance, age=age)
        return HttpResponse(f"Приветствуем, {username}!")

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            result = handle_registration(form)
            return render(request, 'registration_page.html', result)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})
# Create your views here.

def get_platform(request):
    return render(request, "platform.html")
def get_cart(request):
    return render(request, "cart.html")
def get_games(request):
    Games = ["Cyberpunk 2077, Game of the year, Стоимость: 31",
             "Hitman, Who kills Mark?, Стоимость: 80",
             "Mario, Old Game, Стоимость: 5"]

    # descr = ["Game of the year", "Who kills Mark?", "Old Game"]
    # co_s = ["31", "80", "5"]
    context = {
        'Games': Games,
        # 'descr': descr,
        # 'co_s': co_s,
    }

    return render(request, "games.html", context=context)
def get_menu(request):
    return render(request, "menu.html")
# Create your views here.