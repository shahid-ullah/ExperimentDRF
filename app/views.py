# app/views.py
from django.http import HttpResponse
from django.shortcuts import render

from .forms import post_form
from .models import Post


def post_new_view(request):
    form = post_form()

    if request.method == 'POST':
        form =post_form(request.POST)
        breakpoint()
        HttpResponse('post request accepted')
    return render(request, 'post_new.html', {'form': form})
