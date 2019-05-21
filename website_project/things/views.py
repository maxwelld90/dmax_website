from django.shortcuts import render, redirect
from django.http import HttpResponse
from dmax_org_uk import utils
from . import models

def landing(request):
    context_dict = {'things': models.Thing.objects.all().order_by('display_order')}
    
    return render(request, template_name='things/landing.html', context=context_dict)

def phd(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'diagram')
    
    return render(request, template_name='things/phd/landing.html', context=context_dict)

def phd_experiences(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'jeir')
    
    return render(request, template_name='things/phd/experiences.html', context=context_dict)

def phd_journey(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'jeir')
    
    return render(request, template_name='things/phd/journey.html', context=context_dict)

def phd_writing_up(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'jeir')
    
    return render(request, template_name='things/phd/writing-up.html', context=context_dict)

def entry(request, thing_slug):
    """
    Default fallback view for viewing a particular slug.
    """
    try:
        thing = models.Thing.objects.get(slug=thing_slug)
    except models.Thing.DoesNotExist:
        return redirect('things:landing')
    
    if thing.url_type != models.Thing.THING_URL_INTERNAL:
        return redirect('things:landing')
    
    return HttpResponse("thing " + thing_slug)