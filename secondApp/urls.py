from django.urls import path

from secondApp.views import feeCollection
from secondApp.views import feeCollectionReport
from secondApp.views import feeDuesReport 

urlpatterns = [
  

    path('feecol/', feeCollection),
    path('feedues/', feeDuesReport),
    path('feecolrep/', feeCollectionReport),
]