from collective.behavior.price import _
from moneyed.classes import CURRENCIES
from zope import schema
from zope.interface import Attribute
from zope.interface import Interface


class IPrice(Interface):
    """Add salable field to dexterity type.
    """

    price = schema.Decimal(
        title=_(u"Price"),
        required=True)

    currency = Attribute('Currency like EUR')
    money = Attribute('Money instance')


currencies = CURRENCIES.keys()
currencies.sort()


class ICurrency(Interface):

    default_currency = schema.Choice(
        title=_(u'Default Currency'),
        description=_(u'Default Currency for price field.'),
        required=True,
        values=currencies,
        default='EUR')
