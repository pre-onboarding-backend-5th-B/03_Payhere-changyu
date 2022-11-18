from django.db import models
from django.core.validators import MinValueValidator

from user.models import User


class AccountBook(models.Model):
    class StatusChoices(models.TextChoices):
        INCOME = "I", "수입"
        EXPENDITURE = "E", "지출"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    memo = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=StatusChoices.choices, blank=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "account_book"
