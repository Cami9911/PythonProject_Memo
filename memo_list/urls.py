from django.urls import path
from . import views

urlpatterns = [
    path('', views.addItem, name="addItem"),
    path('about/', views.aboutPage, name="aboutPage"),
    path('deleteItem/<list_id>', views.deleteItem, name="deleteItem"),
    path('editItem/<list_id>', views.editItem, name="editItem"),
    path('markAsComplete/<list_id>', views.markAsComplete, name="markAsComplete"),
    path('markAsIncomplete/<list_id>', views.markAsIncomplete, name="markAsIncomplete"),

]
