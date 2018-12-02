from django.urls import path, re_path

from home.views import HomeView, AddFullTermChildView, UpdateChildView, DeleteChildView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', HomeView.as_view(), name='home'),
    path('add_child/', AddFullTermChildView.as_view(), name='add_child'),
    path('details_child/<int:pk>/', UpdateChildView.as_view(), name='update_child'),
    re_path(r'del_child/(?P<pk>\d+)/$', DeleteChildView.as_view(), name='del_child'),
]
