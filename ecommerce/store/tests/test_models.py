from django.test import TestCase
from decimal import Decimal
from django.core.files.uploadedfile import SimpleUploadedFile
from store.models import Item, Employee, Sale, UpdatedItemPrice

class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Employee.objects.create(name='Employee1')
    
    def test_name_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Продавец')
    
    def test_name_max_length(self):
        employee = Employee.objects.get(id=1)
        max_length = employee._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
    
    def test__str__representation(self):
        employee = Employee.objects.get(id=1)
        self.assertEquals(str(employee),'Employee1')
        

class ItemModelTest(TestCase):

    def setUp(self):
        self.item = Item.objects.create(
            title='Phone', 
            slug='phone', 
            image= SimpleUploadedFile('phone_image.jpg', content=b'', content_type='image/jpg'), 
            price= Decimal(1200)
        )
    
    def test_title_label(self):
        field_label = self.item._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'Наименование')
    
    def test_title_max_length(self):
        max_length = self.item._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)
    
    def test_price_label(self):
        field_label = self.item._meta.get_field('price').verbose_name
        self.assertEquals(field_label,'Цена')
    
    def test_price_max_length(self):
        max_digits = self.item._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 9)
    
    def test_update_price_correct_saved(self):
        current_price = self.item.price
        # update_price
        self.item.price = 2500
        self.item.save(update_fields=['price'])
        self.assertEquals(current_price, 1200)
        self.assertEquals(self.item.price, 2500)


class SaleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        employee = Employee.objects.create(name='Employee1')
        item = Item.objects.create(
                title='Phone', 
                slug='phone',
                image= SimpleUploadedFile('phone_image.jpg', content=b'', content_type='image/jpg'), 
                price= Decimal(1200)
                )
        Sale.objects.create(item = item, employee= employee, qty=2)
    
    def test_item_label(self):
        sale = Sale.objects.get(id=1)
        field_label = sale._meta.get_field('item').verbose_name
        self.assertEquals(field_label,'Товар')
   
    def test_employee_label(self):
        sale = Sale.objects.get(id=1)
        field_label = sale._meta.get_field('employee').verbose_name
        self.assertEquals(field_label,'Продавец')
    
    def test_qty_label(self):
        sale = Sale.objects.get(id=1)
        field_label = sale._meta.get_field('qty').verbose_name
        self.assertEquals(field_label,'Количество')

    def test_get_total_price(self):
        sale = Sale.objects.get(id=1)
        total_price = sale.item.price * sale.qty
        self.assertEqual(total_price, 2400)