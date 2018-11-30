from django.urls import path

from home.views import HomeView, AddFullTermChildView, UpdateChildView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', HomeView.as_view(), name='home'),
    path('add_child/', AddFullTermChildView.as_view(), name='add_child'),
    path('details_child/<int:pk>/', UpdateChildView.as_view(), name='update_child'),
]
