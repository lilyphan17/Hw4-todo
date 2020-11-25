from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TaskForm
from .models import Todo


def index(request):
    tasks = Todo.objects.all()  # Get all the record in the todo table
    form = TaskForm()  # Makes a blank form
    context = {'tasks': tasks, 'form': form}  # Context for index.html
    return render(request, 'Todo/index.html', context)


def add(request):
    task = request.POST.get('task')  # Get the name of the tasks to add into the database
    if len(task):  # If user writes anything, a number higher than zero
        Todo.objects.create(task=task)  # Insert task into the table todo
        return redirect('index')
    else:  # If user writes nothing and tries to add, do nothing
        return redirect('index')


def update(request, task_id):
    task = Todo.objects.get(pk=task_id)  # Gets the object with that ID
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Make form with the objects name
        if form.is_valid():
            q = form.cleaned_data  # Make a dictionary with cleaned data
            task.task = q['task']  # Updates the name of the task
            task.completed = q['completed']  # Changes statue to selected value
            task.completed = q['completed']  # Changes statue to selected value
            task.save()  # Saves changes to object
            return redirect('index')
    else:
        form = TaskForm(initial={'task': task.task})  # Makes a blank form with initial task name
        context = {'task': task, 'form': form}  # Context for update.html
        return render(request, 'Todo/update.html', context)


def delete(request, task_id):
    task = Todo.objects.get(pk=task_id)  # Gets the object with that ID

    if request.method == 'POST':
        delete_message = task.task + " has been removed."
        task.delete()  # Delete the object
        messages.info(request, delete_message)
        return redirect('index')
    else:
        context = {'task': task}  # Context for delete.html
        return render(request, 'Todo/delete.html', context)


def complete_task(request, task_id):
    task = Todo.objects.get(pk=task_id)  # Gets the object with that ID
    update_message = task.task + " has been completed."
    task.completed = True  # Check complete status
    task.save()  # Save the list
    messages.info(request, update_message)
    return redirect('index')