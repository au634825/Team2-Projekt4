"""
Contains view functions for the demo_module
URL paths that lead here are in demo_module/urls.py
"""
import time

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.template import loader
from datetime import datetime
from django.conf import settings
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
import locale

from comms.messagehandler.client import MqttClient
from comms.messagehandler import protocol
from .forms import TestForm, AccelerometerForm, PanelAngleForm
from .models import Result, Status
from .models import Inbound_teststand_package, Test_stand_data, Test_stand_parameters, ND_TS

# Bokeh for charts
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, ResetTool, FreehandDrawTool

# Numpy for data
import numpy as np
from numpy import fft as fft

# CSV writer without writing to a file on disk
import csv
import io

import json


def receive_mqtt():
    def on_message(client, userdata, message):
        print(message.topic + " " + str(message.payload))
        global returnData
        returnData = eval(message.payload.decode("utf-8"))

        global receiving
        receiving = False
        pass

    # Callback on publishing - After handshakes
    def on_publish(client, userdata, mid):
        global sending
        sending = False

    # Create client
    receiver = MqttClient("Team2ModuleMessageSender", on_message, on_publish)
    # Send and disconnect
    topic = "Testdevice/team2_module/REQUEST"
    send_me = "SEND_DATA"
    rc = receiver.publish(topic, send_me)
    receiver.subscribe("Testdevice/team2_module/DATA")
    receiver.loop_start()
    global sending
    sending = True
    # Wait for the handshaking to end
    while sending:
        pass

    global receiving
    receiving = True
    # Wait for the handshaking to end
    while receiving:
        time.sleep(0.1)
        pass
    receiver.loop_stop()
    receiver.disconnect()

    return rc, returnData


def transmit_mqtt(form_obj):
    """
    This function is not a view.
    This function transmits a validated message.
    Jenath, feb 2021
    """
    # Print to console for debug
    print(form_obj)
    # Create a message to send
    topic = 'Testdevice/team2_module/RECEIVE'
    send_me = [topic,
               form_obj['sender'],
               form_obj['angle'],
               form_obj['brightness'],
               form_obj['resistance']
               ]
    # debug output to console
    print("før!!")
    print(send_me)
    send_me = str(send_me)
    print("Efter!!")

    # Send it

    # The donothing callback function
    def donothing(client, userdata, message):
        pass

    # Callback on publishing - After handshakes
    def on_publish_callback(client, userdata, mid):
        global sending
        sending = False

    # Create client
    publisher = MqttClient("Team2oduleMessageSender", donothing, on_publish_callback)

    # Send and disconnect
    rc = publisher.publish(topic, send_me)

    publisher.loop_start()
    global sending
    sending = True
    # Wait for the handshaking to end
    while sending:
        pass
    publisher.loop_stop()

    publisher.disconnect()

    return rc


def team2_main_page(request):
    if request.method == 'POST':
        output = PanelAngleForm(request.POST)
        print("Angle changed of solar panel to:", request.POST['angle'], "!")
        # Attempt to transmit MQTT-message based on validated output data
        print(output.is_valid())
        if output.is_valid():
            if transmit_mqtt(output.cleaned_data):
                print("!!!!!Succes. Beskeden blev sendt. med mqtt")
                outcome = "Succes. Beskeden blev sendt."
            else:
                outcome = "Fejl. Beskeden blev ikke."

        voltage = 1
        current = 1
        power = voltage * current
        resistance = output.cleaned_data['resistance']
        irradiance = 1
        temperature = 1

        time.sleep(4)

        receiveStatus, returnData = receive_mqtt()
        if receiveStatus:
            print('beaglebone modtog data request')
            voltage = returnData[0]
            current = returnData[1]
            power = returnData[2]
            # resistance = returnData[3]
            irradiance = returnData[4]
            temperature = returnData[5]
        else:
            print('beaglebone modtog IKKE data request')

        context = {'output': output,
                   'voltage': voltage,
                   'current': current,
                   'power': power,
                   'resistance': resistance,
                   'irradiance': irradiance,
                   'temperature': temperature,
                   }

        return render(request, 'team2_module/home.html', context)
    elif request.GET.get('updateBtn'):
        print("UpdateBtn pressed")
        voltage = 1
        current = 1
        power = voltage * current
        resistance = round(voltage / current, 2)
        irradiance = 1
        temperature = 1

        receiveStatus, returnData = receive_mqtt()
        if receiveStatus:
            print('beaglebone modtog data request')
            voltage = returnData[0]
            current = returnData[1]
            power = returnData[2]
            resistance = returnData[3]
            irradiance = returnData[4]
            temperature = returnData[5]
        else:
            print('beaglebone modtog IKKE data request')

        output = PanelAngleForm()
        context = {'output': output,
                   'voltage': voltage,
                   'current': current,
                   'power': power,
                   'resistance': resistance,
                   'irradiance': irradiance,
                   'temperature': temperature,
                   }

        return render(request, 'team2_module/home.html', context)

    else:
        output = PanelAngleForm()
        return render(request, 'team2_module/home.html', {'output': output})
