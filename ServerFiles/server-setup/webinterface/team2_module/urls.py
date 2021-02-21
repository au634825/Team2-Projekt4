"""
Contains URL routes for the demo_module
All URL paths are <server>/demo_module/<defined_route>

Django 2.2 uses the function path, not url.
"""

from django.urls import path
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    #/team2_module/
    path('',views.team2_main_page,name='team2_home'),

    # /team2/panel_angel
  #  path('panel_angel', views.panel_angel, name='team2_panel_angle'),


    #path for MQTT
    #path('',views.send_mqtt,name='demo_modul')
]
