from django.test import TestCase
from django.urls import reverse


class ServiceIndexViewTests(TestCase):
    def no_error(self):
        url = reverse('service:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
