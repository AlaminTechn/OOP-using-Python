
# In Python Django, method overloading and method overriding can be observed in class-based views, serializers, or models. Below are practical examples of both concepts:
# Scenario: Customizing the behavior of Django's save method in a model.

from .models import Product
from django.views.generic import ListView
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    # Overriding the save method
    def save(self, *args, **kwargs):
        # Ensuring the first name is always stored in lowercase
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()
        super().save(*args, **kwargs)  # Call the original save method


# Usage in views or shell
user = User(first_name="John", last_name="DOE", email="john.doe@example.com")
user.save()

# Query the database
print(user.first_name)  # Output: john
print(user.last_name)   # Output: doe


# Explanation:
# The save method is overridden in the User model.
# Custom logic (e.g., converting names to lowercase) is added before calling super().save(), which ensures the default save functionality is preserved.


"""
======== second ecample ======
"""


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"

    # Overriding get_queryset
    def get_queryset(self):
        # Return only active products
        return Product.objects.filter(is_active=True)


"""
Explanation:
Default Behavior: The get_queryset method in ListView fetches all records from the model.
Overriding: The get_queryset method is overridden to fetch only active products.
"""
