from django import forms
from django.forms import HiddenInput, TextInput

from accounts.models import User
from home.models import Child, Section, Category, ClothingItem, ShoeItem, Item


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
        self.fields['date_of_birth'].widget = TextInput(attrs={'class': 'dp'})
        self.fields['size_system'].widget = HiddenInput()
        self.initial['child_status'] = Child.F
        self.fields['child_status'].widget = HiddenInput()
        self.fields['due_date'].widget = HiddenInput()


class PreemieForm(forms.ModelForm):

    class Meta:
        model = Child
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PreemieForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = True
        self.fields['gender'].required = True
        self.fields['due_date'].required = True

        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.initial['user'] = User.objects.filter(pk=user.pk).first()
        self.fields['user'].widget = HiddenInput()
        self.fields['date_of_birth'].widget = TextInput(attrs={'class': 'dp'})
        self.fields['size_system'].widget = HiddenInput()
        self.initial['child_status'] = Child.P
        self.fields['child_status'].widget = HiddenInput()
        self.fields['due_date'].widget = TextInput(attrs={'class': 'dp_due_date'})


class NotBornChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(NotBornChildForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].required = True

        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.initial['user'] = User.objects.filter(pk=user.pk).first()
        self.fields['user'].widget = HiddenInput()
        self.fields['size_system'].widget = HiddenInput()
        self.initial['name'] = "Coming Soon"
        self.fields['name'].widget = HiddenInput()
        self.initial['child_status'] = Child.N
        self.fields['child_status'].widget = HiddenInput()
        self.fields['due_date'].widget = TextInput(attrs={'class': 'dp_due_date'})


class UpdateSizeSystemForm(forms.ModelForm):
    class Meta:
        model = Child
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
        model = Child
        fields = ['user', 'name', 'size_system', 'corrected_sizes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(UpdateSizesForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.initial['user'] = User.objects.filter(pk=user.pk).first()
        self.fields['user'].widget = HiddenInput()
        self.fields['name'].widget = HiddenInput()
        self.fields['size_system'].widget = HiddenInput()


class UpdateShoeSizesForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['user', 'name', 'size_system', 'corrected_shoe_sizes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(UpdateShoeSizesForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(pk=user.pk)
        self.initial['user'] = User.objects.filter(pk=user.pk).first()
        self.fields['user'].widget = HiddenInput()
        self.fields['name'].widget = HiddenInput()
        self.fields['size_system'].widget = HiddenInput()


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop("pk")
        super(SectionForm, self).__init__(*args, **kwargs)
        self.fields['child'].queryset = Child.objects.all()
        self.initial['child'] = Child.objects.filter(pk=self.pk).first()
        self.fields['child'].widget = HiddenInput()


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop("pk")
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['section'].queryset = Section.objects.all()
        self.initial['section'] = Section.objects.filter(pk=self.pk).first()
        self.fields['section'].widget = HiddenInput()
        self.fields['num_items'].widget = HiddenInput()


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop("pk")
        super(UpdateCategoryForm, self).__init__(*args, **kwargs)
        self.fields['section'].widget = HiddenInput()
        self.fields['num_items'].widget = HiddenInput()


class UpdateSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop("pk")
        super(UpdateSectionForm, self).__init__(*args, **kwargs)
        # self.fields['child'].queryset = Child.objects.all()
        # self.initial['child'] = Child.objects.filter(pk=self.pk).first()
        self.fields['child'].widget = HiddenInput()


class ClothingItemForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = '__all__'


class ShoeItemForm(forms.ModelForm):
    class Meta:
        model = ShoeItem
        fields = '__all__'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

