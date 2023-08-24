from django.urls import path
from products import views

urlpatterns=[
    path('<int:pk>/',views.ProductDetailView.as_view(),name='detail-view'),
    path('',views.ProductCreateView.as_view(),name='create-view'),
    path('all/',views.ProductListView.as_view(),name='list-view'),
    path('all/',views.ProductListView.as_view(),name='list-view'),
    path('update/<int:pk>',views.ProductUpdateView.as_view(),name='update-view'),
    path('delete/<int:pk>',views.ProductDeleteView.as_view(),name='delete-view'),
    path('alt/',views.ProductAltView.as_view(),name='alt-view'),
    path('mixin/',views.ProductMixinView.as_view(),name='mixin-view'),
    path('mixin/<int:pk>/',views.ProductMixinView.as_view(),name='mixin-view'),
]