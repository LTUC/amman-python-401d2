from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Snack

# Create your tests here.

class SnacksCRUDTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'ahmad',
            email = 'ahmad@ahmad.com',
            password = '123456ahmad'
        )
        self.snack = Snack.objects.create(
            name = 'chocolate',
            rank = 10,
            eater = self.user
        )

    def test_snacks_page_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_snack_details_status(self):
        response = self.client.get(reverse('snack_details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_snack_details_content(self):
        response = self.client.get(reverse('snack_details', args='1'))
        self.assertContains(response, 'chocolate')

    def test_snack_update(self):
        response = self.client.post(reverse('snack_update', args='1'), {
            'rank': 8,
        })
        self.assertContains(response, 8)
        self.assertNotContains(response, 10)


# class SnacksTests(TestCase):
#     def test_snacks_page_status(self):
#         # visit the snacks list page
#         url = reverse('home')
#         # '/snacks/'
#         # print(url)
#         # get the response
#         response = self.client.get(url)
#         actual = response.status_code
#         expected = 200
#         self.assertEqual(expected, actual)

#     def test_not_found(self):
#         url = '/snacks/hello'
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)

#     def test_details_page_template(self):
#         url = reverse('snack_details', args='1')
#         print(url)
#         response = self.client.get(url)
#         print(response)
#         self.assertEqual(response.status_code, 200)
