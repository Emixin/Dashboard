from django.urls import path
from .views import HomeView, DashboardView, SignUpView, CustomLoginView, CustomLogoutView, CreateOrder



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('new_order/', CreateOrder.as_view(), name='create_order'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
