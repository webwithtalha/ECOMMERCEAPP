from django.test import TestCase, Client
from django.urls import reverse
from .models import users , products
import json

# Create your tests here.
class UserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_user_url = reverse('create_user')
        self.get_users_url = reverse('get_users')
        self.user_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }

    def test_create_user(self):
        response = self.client.post(
            self.create_user_url,
            data=json.dumps(self.user_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())
        self.assertEqual(response.json()['name'], self.user_data['name'])

    def test_get_users(self):
        # Create a user first
        self.client.post(
            self.create_user_url,
            data=json.dumps(self.user_data),
            content_type='application/json'
        )
        response = self.client.get(self.get_users_url)
        self.assertEqual(response.status_code, 200)
        users_list = response.json()
        self.assertEqual(len(users_list), 1)
        self.assertEqual(users_list[0]['name'], self.user_data['name'])
        self.assertEqual(users_list[0]['email'], self.user_data['email'])

