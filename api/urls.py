from django.conf.urls import url

from api.views import CountryAPI

urlpatterns = [
    url('countries', CountryAPI.as_view(), name='countries'),
]
