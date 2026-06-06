from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from to_do_list_app.forms import TaskForm, TagForm
from to_do_list_app.models import *


class HomePageView(generic.TemplateView):
    template_name = "home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["task_queryset"] = Task.objects.all().order_by(
            "completion_status",
            "-created_at"
        )

        return context

    @staticmethod
    def post(request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        task = Task.objects.get(pk=task_id)
        task.completion_status = not task.completion_status
        task.save()

        return redirect(reverse_lazy("to_do_list:home_page"))


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do_list:home_page")
    template_name = "task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do_list:home_page")
    template_name = "task_form.html"


class TaskDeleteView(generic.DeleteView):
    template_name = "confirm_delete.html"
    model = Task
    success_url = reverse_lazy("to_do_list:home_page")
    context_object_name = "task"


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "tags_list.html"
    queryset = Tag.objects.order_by("name")


class TagsCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("to_do_list:tags_list")
    template_name = "tag_form.html"


class TagsUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("to_do_list:tags_list")
    template_name = "tag_form.html"


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do_list:tags_list")
    context_object_name = "tag"
    template_name = "confirm_delete.html"
