import unittest

from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       expected = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2)
       self.assertEqual(getDataPoint(quote), expected)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       expected = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2)
       self.assertEqual(getDataPoint(quote), expected)


  """ ------------ Add more unit tests ------------ """
  def test_getRation(self):
    price_a = 119.2
    price_b = 117.87
    
    expected = price_a / price_b
    self.assertEqual(getRatio(price_a, price_b), expected)

  def test_getRation_with_price_b_zero(self):
    price_a = 119.2
    price_b = 0

    expected = None
    self.assertEqual(getRatio(price_a, price_b), expected)

  def test_getRation_with_price_a_zero(self):
    price_a = 0
    price_b = 119.2

    expected = price_a / price_b
    self.assertEqual(getRatio(price_a, price_b), expected)


if __name__ == '__main__':
    unittest.main()
