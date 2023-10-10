from django.db import models
from ..customers.models import Customer

COMMUNICATION_TYPES = (
    ('email', 'Email'),
    ('call', 'Call'),
    ('meeting', 'Meeting'),
    ('online meeting', 'Online meeting'),
)

class Communication(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    communication_type = models.CharField(max_length=10, choices=COMMUNICATION_TYPES)
    date = models.DateTimeField()
    notes = models.TextField()
