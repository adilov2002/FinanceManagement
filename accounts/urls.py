from django.urls import path
from . import views


urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('purchases', views.purchases, name='purchases'),

]
