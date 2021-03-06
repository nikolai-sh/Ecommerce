from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

class Item(models.Model):

    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(unique=True)
    image = models.ImageField(default="default.jpg", upload_to="items_image/", verbose_name="Изображение")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")

    class Meta:
        ordering = ["title"]  
   
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

class UpdatedItemPrice(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Товар")
    update_date = models.DateTimeField(verbose_name="Дата обновления цены", auto_now_add=True)
    updated_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Новая цена", blank=True, null=True)
    
    class Meta:
            ordering = ["-update_date"] 
    
    


@receiver(post_save, sender=Item)
def create_updated_item_price(sender, instance, created, **kwargs):
    
    if not created and 'price' in kwargs['update_fields']:
        UpdatedItemPrice.objects.create(item=instance, updated_price=instance.price)

        
        
