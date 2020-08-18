from django.urls import path
from . import views


urlpatterns = [
    #path('<char:name>', views.readlinkresume, name='readlinkresume'),
    path('rfaure', views.rfaure_view), 
]