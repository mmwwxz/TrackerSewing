# production_records/models.py
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    hobby = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class ProductionRecord(models.Model):
    date = models.DateField(auto_now_add=True)
    model = models.CharField(default='',max_length=30, null=True, blank=True)
    name = models.CharField(default='', max_length=30, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    received_by = models.IntegerField(default=0, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default='')

    def save(self, *args, **kwargs):
        # Calculate 'total' before saving
        self.total = self.received_by * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.model} - {self.name}"


class WindowFactoryRecord(models.Model):
    date = models.DateField(auto_now_add=True)
    model = models.CharField(default='', max_length=30, null=True, blank=True)
    name = models.CharField(default='', max_length=30, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    received_by = models.IntegerField(default=0, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate 'total' before saving
        self.total = self.received_by * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.model} - {self.name}"


class WindowExpense(models.Model):
    date = models.DateField(auto_now_add=True)
    window_model_name = models.CharField(max_length=255, null=True, blank=True)
    glass = models.IntegerField(default=0, null=True, blank=True)
    frame = models.IntegerField(default=0, null=True, blank=True)
    fittings = models.IntegerField(default=0, null=True, blank=True)
    installation = models.IntegerField(default=0, null=True, blank=True)
    other = models.IntegerField(default=0, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.total = sum(filter(None, [self.glass, self.frame, self.fittings, self.installation, self.other]))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.window_model_name} - {self.glass} - {self.frame} - {self.fittings} - {self.installation} - {self.other}"


class Expense(models.Model):
    date = models.DateField(auto_now_add=True)
    model_name = models.CharField(max_length=30, default='', null=True, blank=True)
    name_fabric = models.CharField(max_length=30, default='', null=True, blank=True)
    fabric = models.IntegerField(default=0, null=True, blank=True)
    accessories = models.IntegerField(default=0, null=True, blank=True)
    threads = models.IntegerField(default=0, null=True, blank=True)
    other = models.IntegerField(default=0, null=True, blank=True)
    sewing = models.IntegerField(default=0, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total = sum(filter(None, [self.fabric, self.accessories, self.threads, self.other, self.sewing]))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.model_name} - {self.name_fabric} - {self.fabric} - {self.accessories} - {self.threads} - {self.other} - {self.sewing}"
