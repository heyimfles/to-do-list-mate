from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from to_do_list_app.forms import TaskForm
from to_do_list_app.models import *


def home_page(request):
    task_queryset = Task.objects.all().order_by("completion_status").order_by("-created_at")

    context = {
        "task_queryset": task_queryset,
    }

    return render(request, "home_page.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do_list:home_page")
    template_name = "task_form.html"


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "tags_list.html"
    queryset = Tag.objects.order_by("name")
