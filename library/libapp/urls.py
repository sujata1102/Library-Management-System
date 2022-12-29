from django.contrib import admin
from django.urls import path
from libapp import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about, name="about_page"),
    path('books',views.books, name="add_book"),
    path('bookinfo',views.book_info, name="book_info"),
    path('udashboard',views.udashboard, name="udash"),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('studentform',views.studentform),
    path('register',views.user_register, name="user_register"),
    path('login',views.user_login, name="user_login"),
    path('logout',views.user_logout),
    path('getcookies',views.getcookies),
]
