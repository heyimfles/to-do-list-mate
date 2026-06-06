from django.urls import path

from to_do_list_app.views import (
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
    HomePageView,
)


urlpatterns = [
    path(
        "",
        HomePageView.as_view(),
        name="home_page",
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task_create",
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task_update",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_delete",
    ),
    path(
      "tags/",
        TagsListView.as_view(),
        name="tags_list",
    ),
    path(
        "tags/create/",
        TagsCreateView.as_view(),
        name="tags_create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagsUpdateView.as_view(),
        name="tags_update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagsDeleteView.as_view(),
        name="tags_delete",
    ),
]

app_name = "to_do_list"
