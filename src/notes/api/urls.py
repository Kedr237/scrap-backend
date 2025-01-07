from django.urls import include, path

urlpatterns = [
    path("v1/notes/", include("notes.api.v1.urls")),
]
