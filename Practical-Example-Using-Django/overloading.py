"""
Practical Example of Method Overloading in Django
Since Python doesn’t directly support method overloading, we simulate it using optional parameters or arguments.

Scenario: A custom method in a model to fetch user information with different levels of detail.
"""


from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    # Simulated overloading by using optional parameters
    def get_user_info(self, detailed=False):
        if detailed:
            return f"Full Name: {self.first_name} {self.last_name}, Email: {self.email}"
        else:
            return f"Full Name: {self.first_name} {self.last_name}"


# Usage in views or shell
user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
user.save()

# Fetch basic info
print(user.get_user_info())
# Output: Full Name: John Doe

# Fetch detailed info
print(user.get_user_info(detailed=True))
# Output: Full Name: John Doe, Email: john.doe@example.com


"""
Explanation:
The get_user_info method behaves differently based on the detailed parameter.
This simulates method overloading.

"""
