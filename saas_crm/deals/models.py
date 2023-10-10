from django.db import models
from ..customers.models import Customer

DEAL_STAGES = (
    ('prospecting', 'Prospecting'),
    ('lead qualification', 'Lead qualification'),
    ('demo', 'Demo', 'DEMO'),
    ('proposal', 'Proposal'),
    ('commitment', 'Commitment'),
    ('closing', 'Closing'),
    ('retention', 'Retention'),
)

class Deal(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deal_value = models.DecimalField(max_digits=10, decimal_places=2)
    deal_stage = models.CharField(max_length=20, choices=DEAL_STAGES)
    expected_closing_date = models.DateField()
