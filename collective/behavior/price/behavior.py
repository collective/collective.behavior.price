from collective.behavior.price.interfaces import ICurrency
from collective.behavior.price.interfaces import IPrice
from decimal import Decimal
from moneyed import Money
from plone.directives import form
from plone.registry.interfaces import IRegistry
from rwproperty import getproperty
from rwproperty import setproperty
from zope.component import getUtility
from zope.interface import alsoProvides
from zope.interface import implements

import logging

logger = logging.getLogger(__name__)


alsoProvides(IPrice, form.IFormFieldProvider)


class Price(object):
    """
    """
    implements(IPrice)

    def __init__(self, context):
        self.context = context

    @getproperty
    def price(self):
        return getattr(self.context, 'price', None)

    @setproperty
    def price(self, value):
        """Setting price as Decimal and money as Money.

        :param value: Price value such as 5.00, 5,00 nor 1800.
        :type value: str
        """
        if isinstance(value, Decimal):
            # Set price
            setattr(self.context, 'price', value)
            # Set money
            setattr(
                self.context, 'money', Money(value, currency=self.currency))
        else:
            raise ValueError('Not Decimal.')

    @property
    def currency(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(ICurrency).default_currency

    @getproperty
    def money(self):
        return getattr(self.context, 'money', None)

    @setproperty
    def money(self, value):
        """Setting money as Money.

        :param value: Money instance.
        :type value: moneyed.Money
        """
        if isinstance(value, Money):
            setattr(self.context, 'money', value)
        else:
            raise ValueError('Not Money.')
