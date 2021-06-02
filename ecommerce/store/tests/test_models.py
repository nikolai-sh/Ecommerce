from django.test import TestCase

from store.models import Item, Employee, Sale

class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Employee.objects.create(name='Employee1')
    
    def test_name_label(self):
        author = Employee.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Продавец')
    
    def test_name_max_length(self):
        employee = Employee.objects.get(id=1)
        max_length = employee._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

class ItemModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Item.objects.create(title='Phone', slug='phone', image='image.jpeg', price=1200)
    
    def test_title_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'Наименование')
    
    def test_title_max_length(self):
        item = Item.objects.get(id=1)
        max_length = item._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)
    
    def test_price_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('price').verbose_name
        self.assertEquals(field_label,'Цена')
    
    def test_price_max_length(self):
        item = Item.objects.get(id=1)
        max_digits = item._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 9)

class SaleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        employee = Employee.objects.create(name='Employee1')
        item = Item.objects.create(title='Phone', slug='phone', image='image.jpeg', price=1200)
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
