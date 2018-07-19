from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add = True)