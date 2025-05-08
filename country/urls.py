from django.conf.urls import url
from .views import countries_home, country_details, homepage, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', homepage, name='homepage'),
    url(r'^countries/$', countries_home, name='countries'),
    url(r'^countries/(?P<country_id>\d+)/$', country_details, name='countryDetails'),
    url('login/', CustomLoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
