from django.urls import path

from .views import Index

urlpatterns = [
    path(
        "",
        Index.as_view(),
        name="home-index",
    ),
    path(
        "contact-us/",
        Index.as_view(),
        name="contact-us",
    ),
    path(
        "blog/",
        Index.as_view(),
        name="blog",
    )
]
