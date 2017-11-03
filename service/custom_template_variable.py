from .models import AppSettings
import pprint


def settings_processor(request):
    settings = AppSettings.objects.all()
    return {'settings': settings}
