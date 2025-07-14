from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
	now = datetime.datetime.now()
	html = '<html lang="en"><body>It is now.</body></html>'
	return HttpResponse(html)