from django.shortcuts import render
from django.http import HttpResponse
from dmax_org_uk import utils
from . import models

def landing(request):
    context_dict = {'things': models.Thing.objects.all().order_by('display_order')}
    utils.apply_background_to_context(context_dict, 'jeir')
    
    return render(request, template_name='things/landing.html', context=context_dict)

def entry(request, thing_slug):
    return HttpResponse("thing " + thing_slug)