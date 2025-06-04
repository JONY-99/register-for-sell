from django.db import models

class UserModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(max_length=15, null=True, blank=False)

    def __str__(self):
        return self.first_name
