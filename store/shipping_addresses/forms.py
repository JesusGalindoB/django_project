from django.forms import ModelForm

from .models import ShippingAdrress

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAdrress
        fields = [
            'line1', 'line2', 'city', 'state', 'country', 'postal_code', 'reference'
        ]
