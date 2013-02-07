import unittest


class TestICurrency(unittest.TestCase):

    def test_subclass(self):
        from zope.interface import Interface
        from collective.behavior.price.behavior import ICurrency
        self.assertTrue(issubclass(ICurrency, Interface))

    def get_schema(self, name):
        """Get schema of ICurrency interface.

        :param name: Name of schema.
        :type name: str
        """
        from collective.behavior.price.interfaces import ICurrency
        return ICurrency.get(name)

    def test_default_currency__instance(self):
        from zope.schema import Choice
        schema = self.get_schema('default_currency')
        self.assertTrue(isinstance(schema, Choice))

    def test_default_currency__title(self):
        schema = self.get_schema('default_currency')
        self.assertEqual(schema.title, u'Default Currency')

    def test_default_currency__description(self):
        schema = self.get_schema('default_currency')
        self.assertEqual(
            schema.description, u'Default Currency for price field.')

    def test_default_currency__required(self):
        schema = self.get_schema('default_currency')
        self.assertTrue(schema.required)

    def test_default_currency__value(self):
        schema = self.get_schema('default_currency')
        from collective.behavior.price.interfaces import currencies
        keys = schema.vocabulary.by_token.keys()
        keys.sort()
        self.assertEqual(keys, currencies)

    def test_default_currency__default(self):
        schema = self.get_schema('default_currency')
        self.assertEqual(schema.default, 'EUR')
