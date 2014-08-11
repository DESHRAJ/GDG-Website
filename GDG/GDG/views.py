<<<<<<< HEAD

from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, \
    HttpResponseRedirect, HttpResponseNotFound
from django.conf import settings
import json
=======
>>>>>>> 0c1c288339fb2536a9d5dbd259d0a4f3cf8d8572
# Create your views here.
def contactus(request):
	return HttpResponse("soon this page will be available !!!!")

# def home():
<<<<<<< HEAD
# 	return HttpResponse("This page is under construction")
def home(request):    
    """ landing page. """
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', context_instance=RequestContext(request))
=======
# 	return HttpResponse("This page is under construction")
>>>>>>> 0c1c288339fb2536a9d5dbd259d0a4f3cf8d8572
