from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    max_books = models.PositiveIntegerField(default=3)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    # existing fields...
    due_date = models.DateField()
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    extended = models.BooleanField(default=False)  # ← NEW

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = self.borrow_date + timedelta(days=14)
        if self.return_date:
            late_days = (self.return_date - self.due_date).days
            self.fine = max(0, late_days * 10)
        super().save(*args, **kwargs)

