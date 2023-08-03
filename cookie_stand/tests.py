from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import CookieStand


class CookieStandTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1',
                                                         password='pass')
        testuser1.save()

        test_food = CookieStand.objects.create(location="Seattle",
                                             owner=testuser1,
                                        description="Many cookies",
                                        hourly_sales={"9": "5"},
                                        minimum_customers_per_hour=2,
                                        maximum_customers_per_hour=20,
                                        average_cookies_per_sale=6.0)
        test_food.save()

    def test_cookie_stand_model(self):
        stand = CookieStand.objects.get(id=1)
        actual_location = str(stand.location)
        actual_owner = str(stand.owner)
        actual_description = str(stand.description)
        actual_hourly_sales = str(stand.hourly_sales)
        actual_minimum_customers_per_hour = str(stand.minimum_customers_per_hour)
        actual_maximum_customers_per_hour = str(
            stand.maximum_customers_per_hour)
        actual_average_cookies_per_sale = str(stand.average_cookies_per_sale)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_location, "Seattle")
        self.assertEqual(actual_description, "Many cookies")
        self.assertEqual(actual_hourly_sales, "{'9': '5'}")
        self.assertEqual(actual_minimum_customers_per_hour, "2")
        self.assertEqual(actual_maximum_customers_per_hour, "20")
        self.assertEqual(actual_average_cookies_per_sale, "6.0")
