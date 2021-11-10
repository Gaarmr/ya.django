from django.shortcuts import render

from django.http import HttpResponse
from .models import Post

def index(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    response = render(request, 'index.html', {'posts': latest})
    return response


# Create your views here.
