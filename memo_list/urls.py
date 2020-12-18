from django.urls import path
from . import views

urlpatterns = [
    path('', views.addItem, name="addItem"),
    path('deleteItem/<list_id>', views.deleteItem, name="deleteItem"),
    path('edit/<list_id>', views.edit, name="edit"),
    path('markAsComplete/<list_id>', views.markAsComplete, name="markAsComplete"),
    path('markAsIncomplete/<list_id>', views.markAsIncomplete, name="markAsIncomplete"),

]
