from django.conf.urls import url
from .views import countries_home, country_details, homepage

urlpatterns = [
    url(r'^$', homepage, name='homepage'),
    url(r'^countries/$', countries_home, name='countries'),
    url(r'^countries/(?P<country_id>\d+)/$', country_details, name='countryDetails'),
]