from . import utils
from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'shinjuku')
    
    return render(request, template_name='dmax_org_uk/landing.html', context=context_dict)

def me(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'whitelee')
    
    return render(request, template_name='dmax_org_uk/me.html', context=context_dict)

def publications(request):
    return render(request, template_name='dmax_org_uk/publications.html')

def publications_entry(request, publication_slug):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'publication')
    
    return render(request, template_name='dmax_org_uk/publications-entry.html', context=context_dict)

def publications_bibtex(request, publication_slug):
    return HttpResponse("publication bibtex for " + publication_slug)

def thesis(request):
    return HttpResponse("thesis")

def projects(request):
    return HttpResponse("projects")

def projects_entry(request, project_slug):
    return HttpResponse("project " + project_slug)