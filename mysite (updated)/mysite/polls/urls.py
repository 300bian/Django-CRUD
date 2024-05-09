from django.urls import path
from .views import delete_view, update_view, create_view, list_view,main_menu

urlpatterns = [
    path('', main_menu, name='main_menu'),
    path('list/',list_view, name="list"),
    path('create/', create_view, name='geeks_create'),
    path('update/<int:id>',update_view, name='geeks_update'),
    path('delete/<int:id>', delete_view, name='delete_view'),
]