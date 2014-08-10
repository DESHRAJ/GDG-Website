from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, \
    HttpResponseRedirect, HttpResponseNotFound
from pprint import pprint
# for KEYS
from django.conf import settings
import json
from django.template import RequestContext, Context
from django.core.mail import send_mail, BadHeaderError

def home(request):
	return HttpResponse("This page is under construction")
# Create your views here.
def contactus(request):
	return HttpResponse("soon this page will be available !!!!")

