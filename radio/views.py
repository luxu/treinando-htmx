from django.shortcuts import render

from .models import Radio, City


def list_radios(request):
    template_name = 'radio/list_radios.html'
    # template_name = 'radio/hx/radio_result_hx.html'
    radios = Radio.objects.all()
    cities = City.objects.all()
    id_city = 0
    if request.GET.get('id_city'):
        # radios = Radio.objects.filter(cities=request.GET.get('id_city'))
        order_city = City.objects.filter(id=request.GET.get('id_city'))
        radios = Radio.objects.filter(cities=request.GET.get('id_city'))
        id_city = int(request.GET.get('id_city'))
    context = {
        'radios': radios,
        'cities': cities,
        'id_city': id_city
    }
    return render(request, template_name, context)


def add_radios(request):
    template_name = 'radio/list_radios.html'
    name = request.POST['name']
    dial = request.POST['dial']
    Radio.objects.create(
        name=name,
        dial=dial
    )
    radios = Radio.objects.all()
    context = {
        'radios': radios
    }
    return render(request, template_name, context)


def order_radios_by_id(request):
    template_name = 'radio/list_radios.html'
    radios = Radio.objects.all().order_by('id')
    context = {
        'radios': radios
    }
    return render(request, template_name, context)


def order_radios_by_dial(request):
    template_name = 'radio/hx/radio_result_hx.html'
    radios = Radio.objects.all().order_by('-dial')
    context = {
        'radios': radios
    }
    return render(request, template_name, context)

def order_radios_by_name(request):
    template_name = 'radio/list_radios.html'
    radios = Radio.objects.all().order_by('-name')
    context = {
        'radios': radios
    }
    return render(request, template_name, context)
