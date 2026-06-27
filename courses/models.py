from django.db import models
from django.conf import  settings

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name






class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')


    def __str__(self):
        return self.title