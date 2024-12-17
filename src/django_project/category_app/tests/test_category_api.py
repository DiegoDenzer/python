from django.test import TestCase
from rest_framework.test import APITestCase


# Create your tests here.
class TestCategoryAPI(APITestCase):

    def test_list_categories(self):
        response = self.client.get('/api/categories/')

        expected_data = [
            {
                "id": '1',
                "name": 'category.name',
                "description": 'category.description',
                "is_active": True
            }
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)

