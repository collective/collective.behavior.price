import mock
import unittest


class TestPrice(unittest.TestCase):

    def test_class(self):
        from collective.behavior.price.behavior import Price
        self.assertIsInstance(Price, object)

    def create_instance(self, context=mock.Mock()):
        from collective.behavior.price.behavior import Price
        return Price(context)

    def test_instance(self):
        instance = self.create_instance()
        from collective.behavior.price.behavior import Price
        self.assertIsInstance(instance, Price)

    def test_instance_provides_IPrice(self):
        instance = self.create_instance()
        from collective.behavior.price.interfaces import IPrice
        self.assertTrue(IPrice.providedBy(instance))

    @mock.patch('collective.behavior.price.behavior.getUtility')
    def test_instance__verifyObject(self, getUtility):
        instance = self.create_instance()
        from collective.behavior.price.interfaces import IPrice
        from zope.interface.verify import verifyObject
        self.assertTrue(verifyObject(IPrice, instance))

    def test_instance__price_empty(self):
        """First time access to price"""
        context = object()
        instance = self.create_instance(context=context)
        self.assertIsNone(instance.price)

    def test_instance__price_not_empty(self):
        """Price is not empty"""
        context = mock.Mock()
        from decimal import Decimal
        price = Decimal('5.00')
        context.price = price
        instance = self.create_instance(context=context)
        self.assertEqual(instance.price, price)

    def test_instance__set_price__None(self):
        context = mock.Mock()
        price = context.price
        instance = self.create_instance(context=context)
        instance._set_price(None)
        self.assertEqual(instance.price, price)

    def set_price(self, instance, price):
        """Setting price to instance."""
        instance.price = price

    def test_instance__price__ValueError(self):
        """Raise ValueError when setting other than Decimal."""
        instance = self.create_instance()
        self.assertRaises(ValueError, lambda: self.set_price(instance, 'AAA'))

    @mock.patch('collective.behavior.price.behavior.getUtility')
    def test_instance__price__price(self, getUtility):
        """"""
        getUtility().forInterface().default_currency = 'EUR'
        context = mock.Mock()
        instance = self.create_instance(context=context)
        from decimal import Decimal
        price = Decimal('5.00')
        instance.price = price
        self.assertEqual(instance.context.price, price)
        from moneyed import Money
        money = Money(price, currency='EUR')
        self.assertEqual(instance.context.money, money)
        self.assertEqual(instance.money, money)

    @mock.patch('collective.behavior.price.behavior.getUtility')
    def test_instance__currency(self, getUtility):
        """"""
        getUtility().forInterface().default_currency = 'EUR'
        instance = self.create_instance()
        self.assertEqual(instance.currency, 'EUR')

    def test_instance__money_empty(self):
        """First time access to price"""
        context = object()
        instance = self.create_instance(context=context)
        self.assertIsNone(instance.money)

    def set_money(self, instance, money):
        """Setting money to instance."""
        instance.money = money

    def test_instance__money__ValueError(self):
        """Raise ValueError when setting other than Money."""
        instance = self.create_instance()
        self.assertRaises(ValueError, lambda: self.set_money(instance, 'AAA'))

    def test_instance__money__set(self):
        instance = self.create_instance()
        from decimal import Decimal
        from moneyed import Money
        money = Money(Decimal('5.00'), currency="EUR")
        instance.money = money
        self.assertEqual(instance.money, money)

    @mock.patch('collective.behavior.price.behavior.Price.currency', mock.PropertyMock(return_value='EUR'))
    def test__get_money(self):
        from decimal import Decimal
        from moneyed import Money
        instance = self.create_instance()
        instance.context.money = None
        price = Decimal('5.00')
        instance.context.price = price
        self.assertEqual(instance._get_money(), Money(price, currency='EUR'))
