from collective.behavior.price.interfaces import ICurrency
from collective.behavior.price.interfaces import IPrice
from decimal import Decimal
from moneyed import Money
from plone.autoform.interfaces import IFormFieldProvider
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import alsoProvides
from zope.interface import implements


alsoProvides(IPrice, IFormFieldProvider)


class Price(object):
    """Behavior to price content types"""

    implements(IPrice)

    def __init__(self, context):
        self.context = context

    @property
    def price(self):
        return getattr(self.context, 'price', None)

    def _set_price(self, value, name=''):
        """Setting price as Decimal and money as Money for field name.

        :param value: Price value such as 5.00, 5,00 nor 1800.
        :type value: decimal.Decimal

        :param name: Name of field.
        :type name: str
        """
        if value is not None:
            if isinstance(value, Decimal):
                # Set price
                price_name = '{}price'.format(name)
                setattr(self.context, price_name, value)
                # Set money
                money_name = '{}money'.format(name)
                setattr(
                    self.context, money_name, Money(value, currency=self.currency))
            else:
                raise ValueError('Not Decimal.')

    @price.setter
    def price(self, value):
        """Setting price as Decimal and money as Money.

        :param value: Price value such as 5.00, 5,00 nor 1800.
        :type value: decimal.Decimal
        """
        self._set_price(value)

    @property
    def currency(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(ICurrency).default_currency

    def _get_money(self, name=''):
        """Returns money

        :param name: Attribute name infront of money
        :type name: str
        """
        money_name = '{}money'.format(name)
        money = getattr(self.context, money_name, None)
        if money is None:
            price_name = '{}price'.format(name)
            price = getattr(self.context, price_name, None)
            if price is not None:
                money = Money(price, currency=self.currency)
        return money

    @property
    def money(self):
        return self._get_money()

    def _set_money(self, value, name=''):
        """Setting money as Money.

        :param value: Money instance.
        :type value: moneyed.Money

        :param name: Name of field.
        :type name: str
        """
        if isinstance(value, Money):
            money_name = '{}money'.format(name)
            setattr(self.context, money_name, value)
        else:
            raise ValueError('Not Money.')

    @money.setter
    def money(self, value):
        """Setting money as Money.

        :param value: Money instance.
        :type value: moneyed.Money
        """
        self._set_money(value)
