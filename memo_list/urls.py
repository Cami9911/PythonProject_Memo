from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('markAsComplete/<list_id>', views.markAsComplete, name="markAsComplete"),
    path('markAsIncomplete/<list_id>', views.markAsIncomplete, name="markAsIncomplete"),
    path('edit/<list_id>', views.edit, name="edit"),

]
