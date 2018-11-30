from django.urls import path

from accounts import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('acc-settings/<int:pk>/', views.UpdateAccountView.as_view(), name='acc-update'),
]
