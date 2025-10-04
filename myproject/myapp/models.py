from django.db import models

class PaymentAccount(models.Model):
    ACCOUNT_TYPES = [
        ('Bank', 'Bank'),
        ('Wallet', 'Wallet'),
    ]

    account_id = models.AutoField(primary_key=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    bank_name = models.CharField(max_length=100, blank=True, null=True)       # Only for Bank
    account_number = models.CharField(max_length=50, blank=True, null=True)   # Only for Bank
    wallet_provider = models.CharField(max_length=50, blank=True, null=True)  # Only for wallet
    wallet_number = models.CharField(max_length=50, blank=True, null=True)    # Phone/email for wallet

    def __str__(self):
        if self.account_type == "Bank":
            return f"{self.bank_name} ({self.account_number})"
        else:
            return f"{self.wallet_provider} ({self.wallet_number})"
