# type: ignore
# flake8: noqa

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# id(primary key - auto incremented)
# first_name(string), last_name(string), phone(string), email (email), message(text), created_date(date), description(text), category(foreign key), show(boolean), picture(image)

# depois
# owner(foreign key)

# blank=True -> pode ser vazio no form
# null=True -> pode ser nulo no banco de dados


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    callsign = models.CharField(max_length=10)
    saram = models.CharField(max_length=7, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(
        upload_to='pictures/%Y/%m/', blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
