# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import get_object_or_404

from country.models import Country


def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)


# Create your views here.

def countries_home(request):
    countries = Country.objects.values('id','name', 'cca2', 'capital', 'population', 'timezones', 'flags')

    context = {
        'countries': countries,
    }

    return render(request, 'countryList.html', context)

def country_details(request, country_id):
   country = get_object_or_404(Country, id=country_id)
   country_region = getattr(country, 'region', None)
   same_region_countries = Country.objects.filter(region=country_region).exclude(id=country.id)

   languages = list(country.languages.values()) if isinstance(country.languages, dict) else []

   context = { 'country': country, 'same_region_countries': same_region_countries, 'languages': languages }

   return render(request, 'countryDetails.html', context)