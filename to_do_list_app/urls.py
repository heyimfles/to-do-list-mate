from django.urls import path

from to_do_list_app.views import (
    home_page,
    TaskCreateView, TagsListView,
)


urlpatterns = [
    path(
        "",
        home_page,
        name="home_page",
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task_create",
    ),
    path(
      "tags/",
        TagsListView.as_view(),
        name="tags_list",
    ),
]

app_name = "to_do_list"
