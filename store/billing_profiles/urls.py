from django.urls import path

from . import views 

app_name = 'billing_profiles'

urlpatterns = [
    path('', views.BillingProfileListView.as_view(), name='billing_profiles'),
    path('new', views.create, name='create')
]