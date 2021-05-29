from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Item, Employee

class HomePageTest(TestCase):
    
    def setUp(self):
        
        Item.objects.create(title='Phone', slug ='phone',
                            image='images.jpg', price=12000, 
                            employee=Employee.objects.create(
                            name=User.objects.create_user('Employee', password='bar'), 
                            email = 'emp@mail.com'
                                ) 
                            )
   
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        response = self.client.get('/')
        item = Item.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(item.title in str(response.content))