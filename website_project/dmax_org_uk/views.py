from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    context_dict = {
        'background': 'shinjuku',
        'background_identifier': 'Shinjuku, Tokyo, Japan - August 2017'}
    
    return render(request, template_name='dmax_org_uk/landing.html', context=context_dict)

def me(request):
    return HttpResponse("me")

def publications(request):
    return render(request, template_name='dmax_org_uk/publications.html')

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