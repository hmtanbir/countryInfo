# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers import CountrySerializer
from country.models import Country

# Create your views here.

class CountryAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        country_id = request.query_params.get('id')
        country_name = request.query_params.get('name')
        language = request.query_params.get('language')
        country = request.query_params.get('country')
        if country_id:
            country = get_object_or_404(Country, id=country_id)
            serializer = CountrySerializer(country)
            return Response({"message": "data fetched successfully", "data": serializer.data})
        elif country_name:
            country = Country.objects.filter(Q(name__icontains=country_name))
            serializer = CountrySerializer(country, many=True)
            return Response({"message": "data fetched successfully", "data": serializer.data})
        elif language:
            country = Country.objects.filter(Q(languages__icontains=language))
            serializer = CountrySerializer(country, many=True)
            return Response({"message": "data fetched successfully", "data": serializer.data})
        elif country:
            country_region = Country.objects.filter(Q(name__icontains=country)).first().region
            countries = Country.objects.filter(Q(region__contains=country_region))
            serializer = CountrySerializer(countries, many=True)
            return Response({"message": "data fetched successfully", "data": serializer.data})
        else:
          country = Country.objects.all()
          serializer = CountrySerializer(country, many=True)
          return Response({"message": "data fetched successfully", "data": serializer.data})

    def post(self, request):
        data = request.data
        serializer = CountrySerializer(data = data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"message": "data created successfully", "data": serializer.data }, status=status.HTTP_201_CREATED)

    def patch(self, request):
        data = request.data
        country_id = data.get('id')
        if not country_id:
            return Response({"message": "data not updated", "errors": "id is required"}, status=status.HTTP_400_BAD_REQUEST)

        country = get_object_or_404(Country, id=country_id)
        serializer = CountrySerializer(country, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"message": "data updated successfully", "data": serializer.data })


    def delete(self, request):
        country_id = request.data.get('id')
        if not country_id:
            return Response({"message": "data not deleted",
                             "errors": "id is required"},
                            status=status.HTTP_400_BAD_REQUEST)
        country = get_object_or_404(Country, id=country_id)
        country.delete()
        return Response({"message": "data deleted successfully" }, status=status.HTTP_204_NO_CONTENT)

