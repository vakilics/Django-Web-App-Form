from django.db import models

# create class "Form" which is child of model class (inheritance)
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):    # this method will print string re-presentaiton
        return f"{self.first_name} {self.last_name}"