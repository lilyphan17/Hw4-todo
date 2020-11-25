from django import forms

from Todo.models import Todo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'