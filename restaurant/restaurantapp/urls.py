from django.urls import path
from . import views

app_name = 'restaurantapp'
urlpatterns = [
    path('', views.index_page, name='index'),
    path('signup', views.user_signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('home', views.log_home, name='home'),



]
