from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, template_name='dmax_org_uk/landing.html')

def me(request):
    return HttpResponse("me")

def publications(request):
    return HttpResponse("publications")

def publications_entry(request, publication_slug):
    return HttpResponse("publications entry - " + publication_slug)

def publications_bibtex(request, publication_slug):
    return HttpResponse("publication bibtex for " + publication_slug)

def thesis(request):
    return HttpResponse("thesis")

def projects(request):
    return HttpResponse("projects")

def projects_entry(request, project_slug):
    return HttpResponse("project " + project_slug)