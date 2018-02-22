from django.test import TestCase
from django.urls import reverse


class StreamViewTests(TestCase):
    def test_addyoutube200(self):
        url = reverse('add.youtube')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_addtwitch200(self):
        url = reverse('add.twitch')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_streamapi200(self):
        url = reverse('stream.live')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_streamesportapi200(self):
        url = reverse('stream.live.esport')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
