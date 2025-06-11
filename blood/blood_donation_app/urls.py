from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('request_blood/', views.request_blood, name='request_blood'),
    path('become_donor',views.become_donor,name='become_donor'),
    path('profile/',views.profile,name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete-account/', views.delete_account, name='delete_account'),
]