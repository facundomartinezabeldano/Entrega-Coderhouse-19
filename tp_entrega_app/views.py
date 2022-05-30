from django.shortcuts import render
from django.template import Template, Context
from django.template import loader
from .models import Relative


def main_page(request):
    db_payload = Relative.objects.values()
    context = {'db_payload': db_payload}
    view = '/index.html'
    # view = loader.get_template('index.html').render(context=context)
    return render(request, template_name='index.html', context=context)
