from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('menu/',views.MenuPage.as_view(),name='menu'),
    path('menu/<int:pk>/',views.MenuFilteredPage.as_view(),name='menu_filtered'),
]
