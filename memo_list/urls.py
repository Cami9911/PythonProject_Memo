from django.urls import path
from . import views

urlpatterns = [
    path('', views.addItem, name="addItem"),
    path('about/', views.aboutPage, name="aboutPage"),
    path('deleteItem/<id_item>', views.deleteItem, name="deleteItem"),
    path('editItem/<id_item>', views.editItem, name="editItem"),
    path('markAsComplete/<id_item>', views.markAsComplete, name="markAsComplete"),
    path('markAsIncomplete/<id_item>', views.markAsIncomplete, name="markAsIncomplete"),

]
