# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
import requests
from country.models import Country


def fetch_data():
    try:
      print("Start Fetching countries...")
      url = "https://restcountries.com/v3.1/all"
      response = requests.get(url)
      print("Countries data fetched successfully.")
      return response.json()
    except Exception, e:
      raise CommandError(e.message)

def clear_db():
    try:
        print("Clearing old db data...")
        Country.objects.all().delete()
        print("Old data cleared successfully.")
    except Exception, e:
        raise CommandError(e.message)

def import_data(data):
    try:
        print("Start importing data  in DB...")
        for item in data:
            Country.objects.create(
                name=item.get('name'),
                tld=item.get('tld'),
                cca2=item.get('cca2'),
                ccn3=item.get('ccn3'),
                cioc=item.get('cioc'),
                independent=item.get('independent'),
                status=item.get('status'),
                unMember=item.get('unMember'),
                currencies=item.get('currencies'),
                idd=item.get('idd'),
                capital=item.get('capital'),
                altSpellings=item.get('altSpellings'),
                region=item.get('region'),
                subregion=item.get('subregion'),
                languages=item.get('languages'),
                latlng=item.get('latlng'),
                landlocked=item.get('landlocked'),
                borders=item.get('borders'),
                area=item.get('area'),
                demonyms=item.get('demonyms'),
                cca3=item.get('cca3'),
                translations=item.get('translations'),
                flag=item.get('cca3'),
                maps=item.get('maps'),
                population=item.get('population'),
                gini=item.get('gini'),
                fifa=item.get('fifa'),
                car=item.get('car'),
                timezones=item.get('timezones'),
                continents=item.get('continents'),
                flags=item.get('flags'),
                coatOfArms=item.get('coatOfArms'),
                startOfWeek=item.get('startOfWeek'),
                capitalInfo=item.get('capitalInfo'),
                postalCode=item.get('postalCode')
            )
        print("Data imported  in DB successfully.")
    except Exception, e:
        raise CommandError(e.message)

class Command(BaseCommand):
    help = 'Fetches country data and imports in Database table'

    def handle(self, *args, **options):
        try:
            data = fetch_data()
            clear_db()
            import_data(data)
        except Exception, e:
            raise CommandError(e.message)



