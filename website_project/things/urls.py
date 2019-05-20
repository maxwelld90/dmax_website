from django.urls import path, include
from . import views

app_name = 'things'

urlpatterns = [
    path('things/phd-life/', views.phd_life, name='phd-life'),
    path('things/phd-life/journey/', views.phd_life_journey, name='phd-life-journey'),
    path('things/phd-life/writing-up/', views.phd_life_writing_up, name='phd-life-writing-up'),
    path('things/phd-life/experiences/', views.phd_life_experiences, name='phd-life-experiences'),
    path('things/<slug:thing_slug>/', views.entry, name='entry'),
    path('', views.landing, name='landing'),
]
