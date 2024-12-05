from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from .models import Order
from .forms import CreateOrderForm


class CustomLoginView(LoginView):
    template_name = 'main/login.html'


class CustomLogoutView(View):
    def get(self, request):
        return redirect('home')


class HomeView(View):
    def get(self, request):
        return render(request, 'main/home.html')


class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'main/signup.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'main/signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user).order_by('-date')
        orders_count = Order.objects.filter(user=user).count()
        total_price =sum(order.price for order in orders)
        return render(request, 'main/dashboard.html', {'orders': orders, 'orders_count': orders_count, 'total_price': total_price})
    

class CreateOrder(View):
    def get(self, request):
        form = CreateOrderForm()
        return render(request, 'main/order.html', {'form': form})
    def post(self, request):
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.user = request.user
            new_order.save()
            return render(request, 'main/success.html', {'new_order': new_order})
        return redirect('dashboard')