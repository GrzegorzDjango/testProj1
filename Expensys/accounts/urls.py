from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    # login tak musi być skonstrułowany, pierwszy jest do wyświetlenia strony a drugi do postowania
    path('login/', LoginView.as_view(template_name='login.html')),
    path('login', views.login, name='login'),
]