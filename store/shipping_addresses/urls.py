from django.urls import path

from . import views

app_name = 'shipping_addresses'

urlpatterns = [
    path('', views.ShippingAddressListView.as_view(), name='shipping_addresses'),
    path('new', views.create, name='create'),
    path('edit/<int:pk>', views.ShippingAddressUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.ShippingAddressDeleteVew.as_view(), name='delete'),
    path('default/<int:pk>', views.default, name='default')
]