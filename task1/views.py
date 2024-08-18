from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *

# Create your views here.
#Buyer = ["Alice", "bob", "Charlie"]

# def handle_registration(form):
#     username = form.cleaned_data['username']
#     password = form.cleaned_data['password']
#     repeat_password = form.cleaned_data['repeat_password']
#     age = form.cleaned_data['age']
#
#     if password != repeat_password:
#         return {'error': "Пароли не совпадают", 'form': form}
#     elif age < 18:
#         return {'error': "Вы должны быть старше 18", 'form': form}
#     elif username in Buyer:
#         return {'error': "Пользователь уже существует", 'form': form}
#     else:
#         Buyer.append(username)
#         return {'message': f"Приветствуем, {username}!", 'form': UserRegister()}
#
#     Buyer.objects.create(name=username, balance=balance, age=age)
#     return HttpResponse(f"Приветствуем, {username}!")
#
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

        Buyer.objects.create(name=username, balance=balance, age=age)
    return HttpResponse(f"Приветствуем, {username}!")

def sign_up_by_django(request):
    Users = Buyer.objects.all()
    usernames = [i.name for i in Users]
    info = {'error':[]}
    i = 0
    form = UserRegister(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in usernames and password == repeat_password and int(age) >= 18:
                Buyer.objects.create(name=username, age=age)
                context = {'username': username}
                return render(request, 'registration_complite.html', context)
            elif username in usernames:
                i += 1
                info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
                print(info[f'error {i}'])
                return HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
            elif password != repeat_password:
                password_no = True
                i += 1
                info[f'error {i}'] = HttpResponse('Пароли не совпадают', status=400, reason='repeated login')
                print(info[f'error {i}'])
                return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            elif int(age) < 18:
                age_no = True
                i += 1
                info[f'error {i}'] = HttpResponse(
                    f'Вы должны быть старше 18 лет', status=400,
                    reason='insufficient age')
                return HttpResponse(
                    f'Вы должны быть старше 18 лет', status=400,
                    reason='insufficient age')

            #result = handle_registration(form)
            #return render(request, 'registration_page.html', result)
    else:
        form = UserRegister()
        context = {'info': info, 'form': form}
        return render(request, 'registration_page.html', context=context)
# Create your views here.

def get_platform(request):
    return render(request, "platform.html")
def get_cart(request):
    return render(request, "cart.html")
def get_games(request):
    Games = [{"Cyberpunk 2077, Game of the year, Стоимость: 31"},
             {"Hitman, Who kills Mark?, Стоимость: 80"},
             {"Mario, Old Game, Стоимость: 5"}]
    context = {
        'Games': Games,

    }

    return render(request, "games.html", context=context)
def get_menu(request):
    return render(request, "menu.html")
# Create your views here.