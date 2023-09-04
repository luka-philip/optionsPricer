from django.db import models

# Create a model for OptionType (e.g., Call or Put)
class OptionType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create a model for the underlying asset (e.g., Stock)
class Asset(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.symbol

# Create a model for Options
class Option(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    option_type = models.ForeignKey(OptionType, on_delete=models.CASCADE)
    strike_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.asset.name} {self.option_type.name} - Strike: {self.strike_price}, Exp: {self.expiration_date}"

# Create a model for P&L records
class ProfitLoss(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    date = models.DateField()
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.option} - Date: {self.date}, P&L: {self.profit_loss}"
