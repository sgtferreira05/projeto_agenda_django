from django.db import models
from django.utils import timezone
# Create your models here.

# id(primary key - auto incremented)
# first_name(string), last_name(string), phone(string), email (email), message(text), created_date(date), description(text), category(foreign key), show(boolean), picture(image)

#depois
#owner(foreign key)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    saram = models.CharField(max_length=7, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(
        upload_to='pictures/%Y/%m/', blank=True, null=True)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
