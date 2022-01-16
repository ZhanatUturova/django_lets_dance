from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from math import pi


def get_rectangle_area(request, width: int, height: int):
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width: int):
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius: int):
    return render(request, 'geometry/circle.html')


def new_get_rectangle_area(request, width: int, height: int):
    redirect_url = reverse('get-rectangle-area', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def new_get_square_area(request, width: int):
    redirect_url = reverse('get-square-area', args=(width,))
    return HttpResponseRedirect(redirect_url)


def new_get_circle_area(request, radius: int):
    redirect_url = reverse('get-circle-area', args=(radius,))
    return HttpResponseRedirect(redirect_url)
