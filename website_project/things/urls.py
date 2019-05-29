from django.urls import path, include
from . import views

app_name = 'things'

urlpatterns = [
    path('phd/', views.phd, name='phd-life'),
    # path('phd/journey/', views.phd_journey, name='phd-journey'),
    path('phd/writing-up/', views.phd_writing_up, name='phd-writing-up'),
    # path('phd/experiences/', views.phd_experiences, name='phd-experiences'),
    path('<slug:thing_slug>/', views.entry, name='entry'),
    path('', views.landing, name='landing'),
]
