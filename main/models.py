from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='no name')

    def __str__(self):
        return self.name
    

