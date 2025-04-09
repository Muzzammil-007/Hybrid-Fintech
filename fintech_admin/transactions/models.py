# transactions/models.py
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, default='user')

    class Meta:
        db_table = 'user'
        managed = False

    def __str__(self):
        return self.email

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='userId')  # Specify the correct column name
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'transaction'
        managed = False

    def __str__(self):
        return f"Transaction {self.id} - {self.status}"