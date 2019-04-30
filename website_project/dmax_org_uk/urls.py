from django.urls import path, include
from . import views

app_name = 'dmax_org_uk'

urlpatterns = [
    path('me/', views.me, name='me'),
    path('publications/', views.publications, name='publications'),
    path('publications/<slug:publication_slug>/', views.publications_entry, name='publications-entry'),
    path('publications/<slug:publication_slug>/bibtex/', views.publications_bibtex, name='publications-bibtex'),
    path('thesis/', views.thesis, name='thesis'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:project_slug>/', views.projects_entry, name='projects-entry'),
    path('', views.landing, name='landing'),
]
