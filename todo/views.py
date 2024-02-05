from django.contrib import messages
from django.shortcuts import render, redirect

from todo import forms
from todo.models import AddTask


# Create your views here.

def home(request):
    obj = AddTask.objects.all()
    return render(request, 'home.html', {'obj': obj})


def add_task(request):
    form = forms.TaskForm()
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Add Successful.')
            return redirect('home')

        else:
            messages.error(request, 'Invalid Data!')
            print(form.errors)
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'task.html', context=context)


def edit_task(request, pk):
    task = AddTask.objects.get(id=pk)
    form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Update Successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Data!')
            print(form.errors)
            return redirect('home')
    return render(request, 'task.html', {'form': form})


def delete_task(request, pk):
    task = AddTask.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task Delete Successful.')
        return redirect('home')
    return render(request, 'delete.html', {'task': task})
