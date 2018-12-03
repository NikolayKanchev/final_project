from django import forms
from django.forms import HiddenInput, TextInput

from accounts.models import User
from home.models import Child, Preemie, NotBornChild


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        user = kwargs.pop('user')
        super(ChildForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = True
        self.fields['gender'].required = True

        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.initial['user'] = User.objects.filter(pk=user.pk).first()
        self.fields['user'].widget = HiddenInput()
        self.fields['size_system'].widget = HiddenInput()
        # self.fields['child_status'].widget = forms.RadioSelect()
        self.fields['date_of_birth'].widget = TextInput(attrs={'class': 'dp'})
        # self.fields['due_date'].widget = TextInput(attrs={'class': 'dp'})


class PreemieForm(forms.ModelForm):

    class Meta:
        model = Preemie
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PreemieForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = True
        self.fields['gender'].required = True

        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.initial['user'] = User.objects.filter(pk=user.pk).first()
        self.fields['user'].widget = HiddenInput()
        self.fields['size_system'].widget = HiddenInput()
        # self.fields['child_status'].widget = forms.RadioSelect()
        self.fields['date_of_birth'].widget = TextInput(attrs={'class': 'dp'})
        self.fields['due_date'].widget = TextInput(attrs={'class': 'dp_due_date'})


class NotBornChildForm(forms.ModelForm):
    class Meta:
        model = NotBornChild
        fields = ['user', 'name', 'due_date']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(NotBornChildForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.initial['user'] = User.objects.filter(pk=user.pk).first()
        self.fields['user'].widget = HiddenInput()
        self.fields['due_date'].widget = TextInput(attrs={'class': 'dp_due_date'})
        self.initial['name'] = "Coming Soon"
        self.fields['name'].widget = HiddenInput()


class UpdateSizeSystemForm(forms.ModelForm):
    class Meta:
        model = NotBornChild
        fields = ['user', 'name', 'size_system']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(UpdateSizeSystemForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.initial['user'] = User.objects.filter(pk=user.pk).first()
        self.fields['user'].widget = HiddenInput()
        self.fields['name'].widget = HiddenInput()


class UpdateSizesForm(forms.ModelForm):
    class Meta:
        model = NotBornChild
        fields = ['user', 'name', 'size_system', 'corrected_sizes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(UpdateSizesForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.initial['user'] = User.objects.filter(pk=user.pk).first()
        self.fields['user'].widget = HiddenInput()
        self.fields['name'].widget = HiddenInput()
        self.fields['size_system'].widget = HiddenInput()
