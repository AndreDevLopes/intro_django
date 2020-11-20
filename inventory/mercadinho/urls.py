from django.urls import path

from . import views

app_name = "mercadinho"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),


]
