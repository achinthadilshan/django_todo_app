from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from .forms import *

# Create your views here.


@login_required(login_url='/admin/')
def index(request):
    if request.method == 'POST':
        if 'create' in request.POST:
            form = ToDoItemForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = request.user
                form.save()
                messages.success(request, 'New ToDo added successfully.')

        elif 'delete' in request.POST:
            try:
                pk = request.POST.get('delete')
                todo = ToDoItem.objects.get(id=pk)
                todo.delete()
                messages.success(request, 'ToDo deleted successfully.')
            except ObjectDoesNotExist:
                return redirect('main:index')

        elif 'edit' in request.POST:
            try:
                pk = request.POST.get('edit')
                todo = ToDoItem.objects.get(id=pk)
                todo.completed = not todo.completed
                todo.save()
                messages.success(request, 'ToDo updated successfully.')
            except ObjectDoesNotExist:
                return redirect('main:index')

    todos = ToDoItem.objects.order_by('completed', '-updated_at')
    form = ToDoItemForm()

    context = {'todos': todos, 'form': form}
    return render(request, 'index.html', context)
