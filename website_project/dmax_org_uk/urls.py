from django.urls import path, include
from . import views

urlpatterns = [
    path('me/', views.me),
    path('publications/', views.publications),
    path('publications/<slug:publication_slug>/', views.publications_entry),
    path('publications/<slug:publication_slug>/bibtex/', views.publications_bibtex),
    path('thesis/', views.thesis),
    path('projects/', views.projects),
    path('projects/<slug:project_slug>/', views.projects_entry),
    path('', views.landing),
]
