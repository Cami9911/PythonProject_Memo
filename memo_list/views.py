from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def addItem(request):
    if request.method == 'POST':
        form_items = ListForm(request.POST or None)

        if form_items.is_valid():
            form_items.save()
            allItems_list = List.objects.all
            messages.success(request,('Item has been added to memo list!'))
            return render(request, 'home.html', {'allItems_list': allItems_list})
    else:
        allItems_list = List.objects.all
        return render(request, 'home.html', {'allItems_list': allItems_list})

def aboutPage(request):
    return render(request, 'about.html')

def deleteItem(request, id_item):
    item_del = List.objects.get(pk=id_item)
    item_del.delete()
    messages.success(request, ('Item has been deleted from memo list'))
    return redirect('addItem')

def editItem(request, id_item):
    if request.method == 'POST':
        item_edit = List.objects.get(pk=id_item)

        form_items = ListForm(request.POST or None, instance=item_edit)

        if form_items.is_valid():
            form_items.save()
            messages.success(request, ('Item has been edited'))
            return redirect('addItem')
    else:
        item_edit = List.objects.get(pk=id_item)
        return render(request, 'edit.html', {'item': item_edit})

def markAsComplete(request, id_item):
    item_done = List.objects.get(pk=id_item)
    item_done.completed = True
    item_done.save()
    return redirect('addItem')

def markAsIncomplete(request, id_item):
    item_undone = List.objects.get(pk=id_item)
    item_undone.completed = False
    item_undone.save()
    return redirect('addItem')
