from django import forms
from django.forms import HiddenInput, TextInput

from accounts.models import User
from home.models import Child


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ChildForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.initial['user'] = User.objects.filter(pk=user.pk).first()
        self.fields['user'].widget = HiddenInput()
        self.fields['size_system'].widget = HiddenInput()
        # self.fields['child_status'].widget = forms.RadioSelect()
        self.fields['date_of_birth'].widget = TextInput(attrs={'class': 'dp'})
        # self.fields['due_date'].widget = TextInput(attrs={'class': 'dp'})
