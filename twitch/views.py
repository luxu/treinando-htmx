from django.shortcuts import render

from .models import Streamer


def index(request):
    template_name = 'twitch/list_twitch.html'
    search = request.GET.get('search')
    streamers = Streamer.objects.all()
    if search:
        streamers = Streamer.objects.filter(game__name__icontains=search)
    context = {
        'object_list': streamers
    }
    return render(request, template_name, context)
