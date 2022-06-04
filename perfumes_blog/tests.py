from django.test import TestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class TestPerfumeView(TestCase):
    def setUp(self):
        self.client.login(username="testuserone", password="anything")
    
    def test_authetication_required(self):
        self.client.logout()
        url = reverse('perfumes_list')
        # 403 Forbidden
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)