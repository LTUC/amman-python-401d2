from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class SnacksTests(TestCase):
    def test_snacks_page_status(self):
        # visit the snacks list page
        url = reverse('home')
        # '/snacks/'
        # print(url)
        # get the response
        response = self.client.get(url)
        actual = response.status_code
        expected = 200
        self.assertEqual(expected, actual)

    def test_not_found(self):
        url = '/snacks/hello'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_details_page_template(self):
        url = reverse('snack_details', args='1')
        print(url)
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)




# x = 9 variable

# x = 9 attribute
