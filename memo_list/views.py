from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def addItem(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item has been added to memo list!'))
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def deleteItem(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted from memo list'))
    return redirect('addItem')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited'))
            return redirect('addItem')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})

def markAsComplete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('addItem')

def markAsIncomplete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('addItem')

