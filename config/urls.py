from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # django
    path("admin/", admin.site.urls),

    # third-party
    path("rosetta/", include("rosetta.urls")),
]
