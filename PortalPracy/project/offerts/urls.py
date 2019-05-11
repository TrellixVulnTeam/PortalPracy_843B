from django.urls import path
from .views import OffertListView, OffertDetailView, OffertCreateView, ApplicationCreateView
from . import views

app_name = 'offerts'

urlpatterns = [
    path('', OffertListView.as_view(), name = 'index'),
    path('details/<int:pk>/', OffertDetailView.as_view(), name = 'offertDetails'),
    path('new_offert/', OffertCreateView.as_view(), name='new_offert'),
    path('apply/<int:pk>', ApplicationCreateView.as_view(), name='apply'),
]
