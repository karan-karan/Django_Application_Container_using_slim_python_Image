from django.test import TestCase


class ProfileViewTests(TestCase):
    def test_home_renders_profile(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Karan Tanwar')
