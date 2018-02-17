from django.test import TestCase
from django.urls import reverse


class ServiceIndexViewTests(TestCase):
    def test_no_error(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
