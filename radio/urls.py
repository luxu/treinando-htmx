from django.urls import path
from . import views as v

app_name = "radio"

urlpatterns = [
    path("", v.list_radios, name="list-radios"),
    path("", v.order_radios_by_dial, name="order-radios-by-dial"),
    path("", v.order_radios_by_name, name="order-radios-by-name"),
    path("", v.order_radios_by_id, name="order-radios-by-id"),
    path("add/", v.add_radios, name="add-radios"),
]
