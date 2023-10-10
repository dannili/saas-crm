from django.db import models
from ..deals.models import Deal

TASK_TYPES = (
    ('email', 'Email'),
    ('call', 'Call'),
    ('meeting', 'Meeting'),
    ('follow up', 'followup', 'Followup', 'Follow up'),
)

class Task(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TASK_TYPES)
    due_date = models.DateField()
    description = models.TextField()
    is_closed = models.BooleanField(default=False)
