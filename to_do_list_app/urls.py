from django.urls import path

from to_do_list_app.views import (
    home_page,
)


urlpatterns = [
    path(
        "",
        home_page,
        name="home_page",
    )
]

app_name = "to_do_list_app"
