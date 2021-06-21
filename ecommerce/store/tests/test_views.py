from django.test import TestCase
from decimal import Decimal
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from store.models import Item, Employee

class HomePageTest(TestCase):
    
    def setUp(self):       
        Item.objects.create(
            title='Phone', 
            slug ='phone', 
            image= SimpleUploadedFile('phone_image.jpg', content=b'', content_type='image/jpg'), 
            price= Decimal(12000)
            )

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_homepage_content(self):
        response = self.client.get('/')
        item = Item.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(item.title in str(response.content))

class ConfirmSaleViewTest(TestCase):

    def setUp(self):       
        Item.objects.create(
            title='Phone', 
            slug ='phone', 
            image= SimpleUploadedFile('phone_image.jpg', content=b'', content_type='image/jpg'), 
            price= Decimal(12000)
        )

    def test_get(self):
        response = self.client.get('/phone/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='Phone')
    
    def test_post_success(self):
        response = self.client.post('/phone/', data={"employee": 'ATB', "qty": 1})
        self.assertEqual(response.status_code, 200)
        
    
