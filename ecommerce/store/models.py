from django.db import models
from django.urls import reverse

class Item(models.Model):

    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="images/")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
   
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"slug": self.slug})
      

class Employee(models.Model):

    name = models.CharField(max_length=255, verbose_name="Продавец")
    
    def __str__(self) -> str:
        return self.name


class Sale(models.Model):
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Товар")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Продавец")
    qty = models.PositiveIntegerField(default=1, verbose_name="Количество")
    date_sales = models.DateTimeField(verbose_name="Дата продажи", auto_now_add=True)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Общая цена", blank=True, null=True)
   
    class Meta:
        ordering = ["-date_sales"]     
    

    def save(self, *args, **kwargs):
        self.total_price = self.item.price * self.qty
        super(Sale, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Продажа №{self.id}'