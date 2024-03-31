from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from . forms import TableForm
from . models import RestaurantTable
from . models import Food
from . models import Order
# Create your views here.

class HomeView(View):

    def get(self, request):
        form = TableForm(request.GET)
        food_list = Food.food_manager.all()
        if form.is_valid():
            table_object = RestaurantTable.objects.create(
                person_name = form.cleaned_data['person_name'],
                email = form.cleaned_data['email'],
                phone_number = form.cleaned_data['phone_number'],
                date_to_come = form.cleaned_data['date_to_come'],
                time_to_come = form.cleaned_data['time_to_come'],
                number_of_people = form.cleaned_data['number_of_people'],
                message = form.cleaned_data['message']
            )
        context = {
            'form': form,
            'food_list': food_list
        }
        return render(request, 'home.html', context)
    
    def post(self, request):
        form = TableForm(request.POST)
        if form.is_valid():
            table_object = RestaurantTable.objects.create(
                person_name = form.cleaned_data['person_name'],
                email = form.cleaned_data['email'],
                phone_number = form.cleaned_data['phone_number'],
                # date_to_come = form.cleaned_data['date_to_come'],
                # time_to_come = form.cleaned_data['time_to_come'],
                number_of_people = form.cleaned_data['number_of_people'],
                message = form.cleaned_data['message']
            )
            form = TableForm()
            messages.info(request, 'Thanks for booking.table has been reserved for you')
        else:
            messages.error(request, 'problem encountered while booking table!!')
            form = TableForm()
        context = {
            'form': form
        }
        return render(request, 'home.html')
    

def register(request): # function to register users
    if request.method == 'POST':
        firstname = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'the username is in use. pick another one!!!')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'the email is taken. try another one!!!')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name = firstname, username = username, email = email, password = password)
                return redirect('login')
        else:
            messages.error(request, 'the passwords given dont match!!!')
            return redirect('register')
    return render(request, 'register.html')

def login(request): #function to login a user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password incorrect. try again!!!')
            return redirect('login')
    return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='login')
def order(request, pk):
    food = Food.food_manager.get(id=pk)
    order = Order.objects.create(food=food)
    context = {
        'order': order,
        'food': food
    }
    return redirect('home')