from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView

from accounts.forms import UserCreationForm, UserLoginForm
from accounts.models import User
from home.models import Child


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect("/")
    return render(request, "registration/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login_register")


class UpdateAccountView(UpdateView):
    model = User
    template_name = 'registration/update_account.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UpdateAccountView,
                        self).get_context_data(object_list=None, **kwargs)
        context['children'] = Child.objects.filter(user=self.request.user.pk)
        return context
