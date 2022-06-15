from django.urls import path

from . import views as v

app_name = 'twitch'

urlpatterns = [
    path('', v.index, name="list-twitch"),
]
