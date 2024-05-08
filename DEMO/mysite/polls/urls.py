from django.urls import path
from .views import delete_view, update_view, create_view, list_view

urlpatterns = [
    path('list/',list_view, name="list"),
    path('create/', create_view, name='geeks_create'),
    path('<id>/update',update_view, name='geeks_update'),
    path('<id>/delete', delete_view, name='delete_view'),
]