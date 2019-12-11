from django.shortcuts import render

from django.views.generic import ListView

from .models import ShippingAdrress


class ShippingAddressListView(ListView):
    model = ShippingAdrress
    template_name = 'shipping_addresses/shipping_addresses.html'

    def get_queryset(self):
        return ShippingAdrress.objects.filter(user=self.request.user).order_by('-default')

def create(request):
    return render(request, 'shipping_addresses/create.html', {
        
    })