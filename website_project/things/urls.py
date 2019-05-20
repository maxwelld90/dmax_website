from django.urls import path, include
from . import views

app_name = 'things'

urlpatterns = [
    path('things/<slug:thing_slug>/', views.entry, name='entry'),
    path('', views.landing, name='landing'),
]
