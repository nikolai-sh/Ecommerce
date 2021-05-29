from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):

    title = models.CharField(max_length=255, verbose_name="Товар")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="images/")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    employee = models.ForeignKey('Employee', verbose_name="Продавец", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    

class Employee(models.Model):

    name = models.OneToOneField(User, verbose_name="Продавец", on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)

    def __str__(self) -> str:
        return f'{self.name}'

class Sale(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    qty = models.PositiveIntegerField(default=0, verbose_name="Количество")
    date_sales = models.DateTimeField(verbose_name="Дата продажи", auto_now_add=True)
