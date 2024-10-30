from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    
    path('home/', views.home, name="home"),
    path('entry/<str:pk>/', views.entry, name ="entry"),
    path('create-entry/', views.createEntry, name="create-entry"),
    path('update-entry/<str:pk>/', views.updateEntry, name="update-entry"),
    path('delete-entry/<str:pk>/', views.deleteEntry, name="delete-entry"),
]

