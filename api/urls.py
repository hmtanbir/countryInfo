from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import CountryAPI

urlpatterns = [
    url('countries', CountryAPI.as_view(), name='countries'),
    url(r'^token/?$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/?$', TokenRefreshView.as_view(), name='token_refresh'),
]
