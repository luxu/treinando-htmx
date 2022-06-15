from django.urls import path

from . import views as v

app_name = "tasks"

urlpatterns = [
    # path("", v.index, name="index"),
    path("", v.TaskListListView.as_view(), name="tasklist-list"),
    path("filter/", v.TaskListFilterView.as_view(), name="tasklist-filter"),
    path("create/", v.TaskListCreateView.as_view(), name="tasklist-create"),
    path("<slug:slug>/", v.TaskListDetailView.as_view(), name="tasklist-detail"),
    path(
        "<slug:slug>/add_task/", v.TaskListAddTaskView.as_view(), name="tasklist-add-task"
    ),
    # path("tasks/", include("tasker.tasks.urls")),
    # path("radios/", include("radio.urls")),
    # path("twitch/", include("twitch.urls"))
]
