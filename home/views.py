from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from home.forms import ChildForm
from home.models import Preemie, Child, FullTermChild


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
        else:
            obj = Child.objects.filter(user=self.request.user.pk).last()
            context['chosen_child'] = obj

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
