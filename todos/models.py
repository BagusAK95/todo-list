from django.db import models

 # Create Todo Model
class Todo(models.Model):
    description = models.CharField(max_length=250)
