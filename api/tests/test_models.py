from django.test import TestCase
from restaurant.models import OrderDetail, FoodDetail


class OrderTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        OrderDetail.objects.create(
            order_id='123', restaurant_name="Tuckshop",
            ordered_items="[{'itemname': 'set dosa', 'quantity': 1, 'price': 30}]",
            bill_amount='50', order_timestamp="2019-10-21 7:00:23"
            )
        OrderDetail.objects.create(
            order_id='12345', restaurant_name="MTR",
            ordered_items="[{'itemname': 'idli', 'quantity': 2, 'price': 50}]",
            bill_amount='100', order_timestamp="2019-10-21 7:00:23"
            )

    def test_order_detail(self):
        tuckshop_restaurant = OrderDetail.objects.get(restaurant_name='Tuckshop')
        mtr_restaurant = OrderDetail.objects.get(restaurant_name='MTR')
        self.assertEqual(
            tuckshop_restaurant.bill_amount, 50)
        self.assertEqual(
            mtr_restaurant.bill_amount, 100)