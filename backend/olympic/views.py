from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from .serializers import EventSerializer, CountrySerializer
from .models import Event, Country
from datetime import datetime
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def filter_queryset(self, queryset):
        date = self.request.query_params.get('date')

        country = self.request.query_params.get('country')
        is_live = self.request.query_params.get('islive')
        islive = None
        if is_live:
            if is_live == "true":
                islive = True
            else:
                islive = False

        if date:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            queryset = queryset.filter(date__gte=date_obj).order_by('-date')

        if country:
            queryset = queryset.filter(
                Q(country_a=country) | Q(country_b=country))

        if islive != None:
            queryset = queryset.filter(is_live=islive)

        return queryset


class EventMarkLive(APIView):
    def post(self, request, id):
        event = Event.objects.get(id=id)
        event.is_live = True
        event.save()

        return Response({
            "message": "marked live",
            "status": 200
        })


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryUpdateView(APIView):
    def post(self, request, id):
        country = Country.objects.get(id=id)

        gold = self.request.query_params.get('gold')
        silver = self.request.query_params.get('silver')
        bronze = self.request.query_params.get('bronze')
        cheer = self.request.query_params.get('cheer')

        if gold and gold == "true":
            country.gold += 1

        if silver and silver == "true":
            country.silver += 1

        if bronze and bronze == "true":
            country.bronze += 1

        if cheer and cheer == "true":
            country.cheer += 1

        country.save()

        return Response({
            "message": "updated country",
            "status": 200
        })
