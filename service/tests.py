from django.test import TestCase
from django.urls import reverse


class ServiceIndexViewTests(TestCase):
    def test_index200(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cooperation200(self):
        url = reverse('service.cooperation')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
