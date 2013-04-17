import unittest


class TestIPrice(unittest.TestCase):

    def test_subclass(self):
        from zope.interface import Interface
        from collective.behavior.price.behavior import IPrice
        self.assertTrue(issubclass(IPrice, Interface))

    def test_alsoProvides(self):
        from plone.autoform.interfaces import IFormFieldProvider
        from collective.behavior.price.behavior import IPrice
        self.assertTrue(IFormFieldProvider.providedBy(IPrice))

    def get_schema(self, name):
        """Get schema of IPrice interface.

        :param name: Name of schema.
        :type name: str
        """
        from collective.behavior.price.behavior import IPrice
        return IPrice.get(name)

    def test_price__instance(self):
        from zope.schema import Decimal
        schema = self.get_schema('price')
        self.assertTrue(isinstance(schema, Decimal))

    def test_price__title(self):
        schema = self.get_schema('price')
        self.assertEqual(schema.title, u'Price')

    def test_price__required(self):
        schema = self.get_schema('price')
        self.assertTrue(schema.required)

    def test_currency__instance(self):
        from zope.interface import Attribute
        schema = self.get_schema('currency')
        self.assertTrue(isinstance(schema, Attribute))

    def test_currency__doc(self):
        schema = self.get_schema('currency')
        self.assertEqual(schema.getDoc(), 'Currency like EUR')

    def test_money__instance(self):
        from zope.interface import Attribute
        schema = self.get_schema('money')
        self.assertTrue(isinstance(schema, Attribute))

    def test_money__doc(self):
        schema = self.get_schema('money')
        self.assertEqual(schema.getDoc(), 'Instance: moneyed.Money')
