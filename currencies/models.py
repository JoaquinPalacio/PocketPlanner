from django.db import models

# Create your models here.


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    rate_to_usd = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ('can_update_rates', 'Can update currency rates'),
        ]

    def __str__(self):
        return self.name
