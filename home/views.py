from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from home.forms import ChildForm, PreemieForm, NotBornChildForm, UpdateSizeSystemForm, UpdateSizesForm
from home.models import Child, FullTermChild, Preemie, NotBornChild


class HomeView(ListView):
    template_name = 'home/index.html'
    context_object_name = 'children'

    def get_queryset(self):
        return Child.objects.filter(user=self.request.user.pk)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView,
                        self).get_context_data(object_list=None, **kwargs)

        if 'pk' in self.kwargs:
            obj = Child.objects.filter(pk=self.kwargs['pk']).first()
            context['chosen_child'] = obj
            if obj is not None and obj.age is None:
                context['not_born_yet'] = True
            else:
                context['not_born_yet'] = False

        else:
            obj = Child.objects.filter(user=self.request.user.pk).last()
            context['chosen_child'] = obj
            if obj is not None and obj.age is None:
                context['not_born_yet'] = True
            else:
                context['not_born_yet'] = False

        return context


class AddFullTermChildView(CreateView):
    model = FullTermChild
    template_name = 'home/add_full_term_child.html'
    form_class = ChildForm

    def get_success_url(self):
        return reverse('home', args=(self.object.id,))

    def get_form_kwargs(self):
        kwargs = super(AddFullTermChildView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AddPreemieView(CreateView):
    model = Preemie
    template_name = 'home/add_preemie.html'
    form_class = PreemieForm

    def get_success_url(self):
        return reverse('home', args=(self.object.id,))

    def get_form_kwargs(self):
        kwargs = super(AddPreemieView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AddNotBornView(CreateView):
    model = NotBornChild
    template_name = 'home/add_not_born_child.html'
    form_class = NotBornChildForm

    def get_success_url(self):
        return reverse('home', args=(self.object.id,))

    def get_form_kwargs(self):
        kwargs = super(AddNotBornView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdateChildView(UpdateView):
    model = Child
    template_name = 'home/update_child.html'
    form_class = ChildForm

    def get_success_url(self):
        return reverse('home', args=(self.object.id,))

    def get_form_kwargs(self):
        kwargs = super(UpdateChildView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DeleteChildView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Child
    success_url = reverse_lazy('home')

    def test_func(self):
        """ Only let the user access this page if they own the object being deleted"""
        return self.get_object().user == self.request.user


class UpdateSizeSystemView(UpdateView):
    model = Child
    template_name = 'home/update_size_system.html'
    form_class = UpdateSizeSystemForm

    def get_success_url(self):
        return reverse('home', args=(self.object.id,))

    def get_form_kwargs(self):
        kwargs = super(UpdateSizeSystemView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdateSizesView(UpdateView):
    model = Child
    template_name = 'home/update_sizes.html'
    form_class = UpdateSizesForm

    def get_success_url(self):
        return reverse('home', args=(self.object.id,))

    def get_form_kwargs(self):
        kwargs = super(UpdateSizesView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
