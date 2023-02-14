from django.urls import path
from . import views
app_name = 'blogapp'

urlpatterns = [
    path('homepage/', views.home, name='homepage')
]
