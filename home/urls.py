from django.urls import path, re_path

from home.views import HomeView, UpdateChildView, DeleteChildView, AddFullTermChildView, \
    AddPreemieView, AddNotBornView, UpdateSizeSystemView, UpdateSizesView, UpdateShoeSizesView, \
    AddSectionView, AddCategoryView, UpdateCategoryView, UpdateSectionView, DeleteSectionView, \
    DeleteCategoryView, AddClothingItemsView, AddShoeItemsView, AddItemsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', HomeView.as_view(), name='home'),
    path('add_child/', AddFullTermChildView.as_view(), name='add_child'),
    path('add_preemie/', AddPreemieView.as_view(), name='add_preemie'),
    path('add_not_born/', AddNotBornView.as_view(), name='add_not_born'),
    path('details_child/<int:pk>/', UpdateChildView.as_view(), name='update_child'),
    path('size_system/<int:pk>/', UpdateSizeSystemView.as_view(), name='update_size_system'),
    path('sizes_update/<int:pk>/', UpdateSizesView.as_view(), name='update_sizes'),
    path('shoe_sizes_update/<int:pk>/', UpdateShoeSizesView.as_view(), name='update_shoe_sizes'),
    re_path(r'del_child/(?P<pk>\d+)/$', DeleteChildView.as_view(), name='del_child'),
    path('add_section/<int:pk>/', AddSectionView.as_view(), name='add_section'),
    path('add_category/<int:pk>/', AddCategoryView.as_view(), name='add_category'),
    path('update_category/<int:pk>/', UpdateCategoryView.as_view(), name='update_category'),
    path('update_section/<int:pk>/', UpdateSectionView.as_view(), name='update_section'),
    re_path(r'delete_section/(?P<pk>\d+)/$', DeleteSectionView.as_view(), name='delete_section'),
    re_path(r'delete_category/(?P<pk>\d+)/$', DeleteCategoryView.as_view(), name='delete_category'),
    path('add_clothing_items/<int:pk>/', AddClothingItemsView.as_view(), name='add_clothing_items'),
    path('add_shoe_items/<int:pk>/', AddShoeItemsView.as_view(), name='add_shoe_items'),
    path('add_items/<int:pk>/', AddItemsView.as_view(), name='add_items'),

]
