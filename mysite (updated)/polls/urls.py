from django.urls import path
from .views import delete_view, update_view, create_view, list_view,main_menu

urlpatterns = [
    path('', main_menu, name='main_menu'),
    path('list/',list_view, name="list"),
    path('create/', create_view, name='geeks_create'),
    path('<int:id>/update',update_view, name='geeks_update'),
    path('<int:id>/delete', delete_view, name='delete_view'),
]