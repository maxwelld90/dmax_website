from django.urls import path, include
from . import views

app_name = 'dmax_org_uk'

urlpatterns = [
    path('me/', views.me, name='me'),
    path('publications/', views.publications, name='publications'),
    path('publications/<slug:publication_slug>/', views.publications_entry, name='publications-entry'),
    path('publications/<slug:publication_slug>/bibtex/', views.publications_bibtex, name='publications-bibtex'),
    path('thesis/', views.thesis, name='thesis'),
    path('', views.landing, name='landing'),
]
