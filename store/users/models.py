from django.db import models

from django.contrib.auth.models import User

class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []