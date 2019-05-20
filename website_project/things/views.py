from django.shortcuts import render, redirect
from django.http import HttpResponse
from dmax_org_uk import utils
from . import models

def landing(request):
    context_dict = {'things': models.Thing.objects.all().order_by('display_order')}
    utils.apply_background_to_context(context_dict, 'jeir')
    
    return render(request, template_name='things/landing.html', context=context_dict)

def phd_life(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'jeir')
    
    return render(request, template_name='things/phd-life/landing.html', context=context_dict)

def phd_life_experiences(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'jeir')
    
    return render(request, template_name='things/phd-life/experiences.html', context=context_dict)

def phd_life_journey(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'jeir')
    
    return render(request, template_name='things/phd-life/journey.html', context=context_dict)

def phd_life_writing_up(request):
    context_dict = {}
    utils.apply_background_to_context(context_dict, 'jeir')
    
    return render(request, template_name='things/phd-life/writing-up.html', context=context_dict)

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