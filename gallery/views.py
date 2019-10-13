# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
# from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def gallery_of_day(request):
    date = dt.date.today()
    gallery = Image.get_all_images()
    return render(request, 'all-gallery/today-gallery.html', {"date": date,"gallery":gallery})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})

def filter_by_lacation (request,location_id):
    images = Image.filter_by_location(id=location_id)
    return render(request,"all-gallery/location.html", {"images":images})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
