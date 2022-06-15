from django import forms
from django.utils.text import slugify
from .models import TaskList


class TaskListCreateForm(forms.ModelForm):
    slug = forms.CharField(required=False, widget=forms.widgets.HiddenInput())

    class Meta:
        model = TaskList
        fields = ("name", "slug")

    def clean_name(self) -> str:
        name: str = self.cleaned_data["name"]
        slug = slugify(name)
        if TaskList.objects.filter(slug=slug).exists():
            raise forms.ValidationError(f"A Task List with the name {name} exists")
        return name

    def save(self, commit: bool = True) -> TaskList:
        task_list: TaskList = super().save(commit)
        task_list.slug = slugify(task_list.name)
        task_list.save()
        return task_list
