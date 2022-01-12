from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect





def index(request):
    return render(request, 'landing/index.html')














def hello(request):
    # request and context and automatically passed to HttpResponse and HttpResponseRedirect
    content = f'<h1> Hello World! </h1> sent using {request.method}'
    return HttpResponse(content)
