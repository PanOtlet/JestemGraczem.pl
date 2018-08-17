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

    def test_signup200(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login200(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_livestream200(self):
        url = reverse('livestreams')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_youtube200(self):
        url = reverse('youtube', {'page': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gameservers200(self):
        url = reverse('gameservers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
