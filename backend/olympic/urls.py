from django.contrib import admin
from django.urls import path
from .views import EventListView, EventMarkLive, CountryListView, CountryUpdateView

urlpatterns = [
    path('events/', EventListView.as_view(), name="list_events"),
    path('event/<int:id>', EventMarkLive.as_view(), name="mark_live_event"),
    path('countries/', CountryListView.as_view(), name='list_country_detail'),
    path('countries/<int:id>', CountryUpdateView.as_view(),
         name='update_country_detail')
]
