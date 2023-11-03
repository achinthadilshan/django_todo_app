from django import forms
from .models import ToDoItem


class ToDoItemForm(forms.ModelForm):
    todo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full px-3 py-2 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Enter a ToDo', 'autocomplete': 'off'})
    )

    class Meta:
        model = ToDoItem
        fields = ['todo', 'completed']
