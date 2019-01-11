from django.urls import path, re_path

from home.views import HomeView, UpdateChildView, DeleteChildView, AddFullTermChildView, \
    AddPreemieView, AddNotBornView, UpdateSizeSystemView, UpdateSizesView, UpdateShoeSizesView, \
    AddSectionView, AddCategoryView, UpdateCategoryView, UpdateSectionView, DeleteSectionView, \
    DeleteCategoryView, AddItemsView, ItemsView, \
    UpdateItemView, DeleteItemView, PhotoView, UpdateShoeFilterSizesView, UpdateClothingFilterSizesView, \
    UpdateClothingFilterSizesSecondView, UpdateShoeFilterSizesSecondView, AllItemsView

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
    path('add_items/<int:pk>/', AddItemsView.as_view(), name='add_items'),
    path('list_items/<int:pk>/', ItemsView.as_view(), name='items_list'),
    path('list_all_items/<int:pk>/', AllItemsView.as_view(), name='all_items_list'),
    path('update_item/<int:pk>/', UpdateItemView.as_view(), name='update_item'),
    re_path(r'del_item/(?P<pk>\d+)/$', DeleteItemView.as_view(), name='del_item'),
    path('crop/<int:pk>/', PhotoView.as_view(), name='crop-photo'),
    path('update_shoe_filter_size/<int:pk>/', UpdateShoeFilterSizesView.as_view(),
         name='update_shoe_filter_size'),
    path('update_shoe_filter_size_second/<int:pk>/<int:category_pk>/', UpdateShoeFilterSizesSecondView.as_view(),
         name='update_shoe_filter_size_second'),
    path('update_clothing_filter_size/<int:pk>/', UpdateClothingFilterSizesView.as_view(),
         name='update_clothing_filter_size'),
    path('update_clothing_filter_size_second/<int:pk>/<int:category_pk>/', UpdateClothingFilterSizesSecondView.as_view(),
         name='update_clothing_filter_size_second'),

]
