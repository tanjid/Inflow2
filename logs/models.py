from django.db import models
from orders.models import NewOrder
# Create your models here.


class OrderLog(models.Model):
    order = models.ForeignKey(NewOrder, on_delete = models.RESTRICT)
    time = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=250)


