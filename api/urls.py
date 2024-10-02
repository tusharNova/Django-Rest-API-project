
from django.urls import path 

from expense import views

urlpatterns = [
    path('/get-Transaction' , views.get_Transaction)
]
