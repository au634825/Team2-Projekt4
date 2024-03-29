"""
This file defines form control elements for the demo_module
See: https://docs.djangoproject.com/en/2.2/topics/forms/
And: https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html

Consider validation for the JSON
https://stackoverflow.com/questions/44085153/how-to-validate-a-json-object-in-django

"""

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Status


class TestForm(forms.Form):
    PROTOCOL_VERSIONS = (
        ('1.1', 'Ver. 1.1'),
    )

    TOPICS = (
        ('Testdevice/demo_module/Inbound', 'Testdevice/demo_module/Inbound'),
        ('Testdevice/demo_module/Outbound', 'Testdevice/demo_module/Outbound'),
    )

    MSG_TYPES = (
        ('command', 'command'),
        ('data', 'data'),
        ('status', 'status'),
        ('result', 'result'),
    )

    #
    protocol_version = forms.ChoiceField(
        label='Protokol',
        choices=PROTOCOL_VERSIONS
    )

    # mqtt message form
    topic = forms.ChoiceField(
        label='Emne (mqtt)',
        choices=TOPICS,
    )

    msg_type = forms.ChoiceField(
        label='Beskedtype',
        choices=MSG_TYPES
    )

    status_code = forms.ChoiceField(
        label='Statuskode',
        choices=Status.STATUS_CODES
    )

    command_list_str = forms.CharField(
        label='Kommandoer (JSON-streng med liste af key-value pairs)',
        widget=forms.TextInput(attrs={
            'value': '["cmd1", "cmd2"]',
            'placeholder': '["cmd1", "cmd2"]'
        }),
        required=False
    )

    parameter_obj_str = forms.CharField(
        label='Parametre (JSON-streng med liste af key-value pairs)',
        widget=forms.Textarea(attrs={
            'placeholder': '{"param1": "val1", "param2": "val2"}'
        }),
        initial='{"param1": "val1", "param2": "val2"}',
        required=False
    )

    data_obj_str = forms.CharField(
        label='Dataobjekt (JSON-streng med liste af key-value pairs)',
        widget=forms.Textarea(attrs={
            'placeholder': '{ "x": [1,2,3,4,5,6,7,8,9,10], "y": [1,4,9,16,25,36,49,64,81,100] }'
        }),
        initial='{ "x": [1,2,3,4,5,6,7,8,9,10], "y": [1,4,9,16,25,36,49,64,81,100] }',
        required=False
    )

    # Who requested this data
    sender = forms.CharField(
        label='Opretter (navn)',
        required=True,
        widget=forms.TextInput(attrs={
            'value': 'testbruger'
        })
    )

    # tag data to keep it in the db forever
    no_delete = forms.BooleanField(
        label='Gem data permanent',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('protocol_version', css_class='form-group col-md-4 mb-0'),
                Column('topic', css_class='form-group col-md-4 mb-0'),
                Column('msg_type', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('status_code', css_class='form-group col-md-4 mb-0'),
                Column('command_list_str', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            'parameter_obj_str',
            'data_obj_str',
            'sender',
            'no_delete',
            Submit('submit', 'Start test')
        )


class AccelerometerForm(forms.Form):
    """
    Denne klasse implementerer formularen til GUI-demo, som vises på Webinterface
    """
    SENSOR_TYPES = (
        ('adxl345', 'adxl345'),
        ('Kx224', 'Kx224'),
    )

    FREQ_LIST = (
        ('10', '10 Hz'),
        ('100', '100 Hz'),
        ('1000', '1 kHz'),
        ('10000', '10 kHz'),
    )

    sensor_type = forms.ChoiceField(
        label='Sensortype',
        choices=SENSOR_TYPES
    )

    duration = forms.CharField(
        label='Varighed af test (sekunder)',
        widget=forms.TextInput(attrs={
            'value': '10',
            'placeholder': 'Indtast antal sekunder her'
        }),
        required=True
    )

    step = forms.CharField(
        label='Steps',
        widget=forms.TextInput(attrs={
            'placeholder': 'Indtast steps her'
        }),
        required=True
    )

    stepTime = forms.CharField(
        label='Steptime i [ms]',
        widget=forms.TextInput(attrs={
            'value': '10',
            'placeholder': 'Indtast stepTime her'
        }),
        required=True
    )

    stepSize = forms.CharField(
        label='Steptime [int]',
        widget=forms.TextInput(attrs={
            'value': '10',
            'placeholder': 'Indtast stepSize her'
        }),
        required=True
    )

    freq = forms.ChoiceField(
        label='Frekvens [Hz]',
        choices=FREQ_LIST
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'sensor_type',
            'duration',
            'step',
            'stepTime',
            'stepSize',
            'freq',
            Submit('submit', 'En knap :)')
        )


class AccelerometerForm(forms.Form):
    """
    Denne klasse implementerer formularen til GUI-demo, som vises på Webinterface
    """
    SENSOR_TYPES = (
        ('adxl345', 'adxl345'),
        ('Kx224', 'Kx224'),
    )

    FREQ_LIST = (
        ('10', '10 Hz'),
        ('100', '100 Hz'),
        ('1000', '1 kHz'),
        ('10000', '10 kHz'),
    )

    sensor_type = forms.ChoiceField(
        label='Sensortype',
        choices=SENSOR_TYPES
    )

    duration = forms.CharField(
        label='Varighed af test (sekunder)',
        widget=forms.TextInput(attrs={
            'value': '10',
            'placeholder': 'Indtast antal sekunder her'
        }),
        required=True
    )

    step = forms.CharField(
        label='Steps',
        widget=forms.TextInput(attrs={
            'placeholder': 'Indtast steps her'
        }),
        required=True
    )

    stepTime = forms.CharField(
        label='Steptime i [ms]',
        widget=forms.TextInput(attrs={
            'value': '10',
            'placeholder': 'Indtast stepTime her'
        }),
        required=True
    )

    stepSize = forms.CharField(
        label='Steptime [int]',
        widget=forms.TextInput(attrs={
            'value': '10',
            'placeholder': 'Indtast stepSize her'
        }),
        required=True
    )

    freq = forms.ChoiceField(
        label='Frekvens [Hz]',
        choices=FREQ_LIST
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'sensor_type',
            'duration',
            'step',
            'stepTime',
            'stepSize',
            'freq',
            Submit('submit', 'En knap :)')
        )


class PanelAngleForm(forms.Form):
    DEG_LIST = (
        ('0', '0 Deg'),
        ('15', '15 Deg'),
        ('30', '30 Deg'),
        ('45', '45 Deg'),
        ('60', '60 Deg'),
        ('75', '75 Deg'),
        ('90', '90 Deg')
    )
    # TOPICS = (
    #   # topic = (')
    #   ('Testdevice/team2_module/panelangle','Testdevice/team2_module/panelangle'),
    # )
    LIGHT_LIST = (
        ('0', '0 %'),
        ('25', '25 %'),
        ('50', '50 %'),
        ('75', '75 %'),
        ('100', '100 %'),
    )
    # mqtt message form
    # topic = forms.ChoiceField(
    #    label='Emne (mqtt)',
    #    choices=TOPICS,
    # )
    # Who requested this data
    sender = forms.CharField(
        label='Opretter (navn)',
        required=True,
        widget=forms.TextInput(attrs={
            'value': 'testbruger'
        })
    )
    angle = forms.ChoiceField(
        label='Solpanel vinkel',
        choices=DEG_LIST
    )
    brightness = forms.ChoiceField(
        label='Lysstyrke',
        choices=LIGHT_LIST
    )
    resistance = forms.FloatField(
        label="Load modstand (0-924)",
        widget=forms.NumberInput(attrs={
            'loadValue': 'Heltal'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'sender',
            'angle',
            'brightness',
            'resistance',
            # 'topic',
            Submit('submit', 'Opdatér data')
        )


class GetValuesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Submit('getValuesBtn', 'opdatér')
        )
