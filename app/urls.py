from django.contrib import admin
from django.urls import path, include

from tasks.views import index

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("tasks/", include("tasks.urls")),
    path("radios/", include("radio.urls")),
    path("twitch/", include("twitch.urls"))
]


