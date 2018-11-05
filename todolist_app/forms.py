from django.forms import ModelForm

from .models import Todo


class TodoModelForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'priority', 'status', 'user']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'priority': 'Priority',
            'status': 'Status',
            'user': 'User',
        }
