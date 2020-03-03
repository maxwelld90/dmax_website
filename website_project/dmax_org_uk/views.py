from . import utils
from . import models
from django.shortcuts import render, redirect
from django.http import HttpResponse

def landing(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'shinjuku')
    
    return render(request, template_name='dmax_org_uk/landing.html', context=context_dict)

def me(request):
    context_dict = {}
    context_dict['publications'] = models.Publication.objects.all()
    utils.apply_background_to_context(context_dict, 'delft')
    
    return render(request, template_name='dmax_org_uk/me.html', context=context_dict)

def publications(request):
    context_dict = {
        'publications': models.Publication.objects.all().order_by('-published_date')
    }
    
    return render(request, template_name='dmax_org_uk/publications.html', context=context_dict)

def publications_entry(request, publication_slug):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'publication')
    
    try:
        publication = models.Publication.objects.get(slug=publication_slug)
    except models.Publication.DoesNotExist:
        return redirect('dmax_org_uk:publications')
    
    if publication.external_url:
        return redirect('dmax_org_uk:publications')
    
    context_dict['publication'] = publication
    
    if publication.background:
        utils.apply_background_to_context(context_dict, 'custom-background')
    
    return render(request, template_name='dmax_org_uk/publications-entry.html', context=context_dict)

def publications_bibtex(request, publication_slug):
    try:
        publication = models.Publication.objects.get(slug=publication_slug)
    except models.Publication.DoesNotExist:
        return redirect('dmax_org_uk:publications')
    
    try:
        bibtex_resource = publication.get_bibtex_resource()
    except models.PublicationResource.DoesNotExist:
        return redirect('dmax_org_uk:publications-entry', publication_slug)
    
    return HttpResponse(bibtex_resource.bibtex, content_type='text/plain')

def thesis(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'lilybank')
    
    return render(request, template_name='dmax_org_uk/thesis.html', context=context_dict)