from django.template.context_processors import request
import datetime

def get_current_datetime(request):
    value = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return {"datetime" : value }