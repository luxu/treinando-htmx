import django_filters
from django import forms
from django.db import models
from django.db.models.query import QuerySet
from tasks.models import TaskList


class CompletenessChoices(models.TextChoices):
    ALL = "all"
    COMPLETE = "complete"
    NOT_COMPLETE = "not_complete"


class TaskListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    completeness = django_filters.ChoiceFilter(
        choices=CompletenessChoices.choices,
        widget=forms.widgets.RadioSelect,
        empty_label=None,
        method="get_completeness",
    )

    class Meta:
        model = TaskList
        fields = ["name", "completeness"]

    def get_completeness(
        self, queryset: QuerySet[TaskList], field_name: str, value: str
    ) -> QuerySet[TaskList]:
        if value == CompletenessChoices.COMPLETE:
            return queryset.filter(id__in=[tl.id for tl in queryset if tl.is_complete])
        elif value == CompletenessChoices.NOT_COMPLETE:
            return queryset.exclude(id__in=[tl.id for tl in queryset if tl.is_complete])
        return queryset
