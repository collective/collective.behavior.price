from collective.behavior.price import _
from collective.behavior.price.schema import PriceSchema
from moneyed.classes import CURRENCIES
from zope import schema
from zope.interface import Attribute
from zope.interface import Interface


class IPrice(PriceSchema):
    """Interface for behaviro: Price"""

    currency = Attribute('Currency like EUR')
    money = Attribute('Instance: moneyed.Money')


currencies = CURRENCIES.keys()
currencies.sort()


class ICurrency(Interface):

    default_currency = schema.Choice(
        title=_(u'Default Currency'),
        description=_(u'Default Currency for price field.'),
        required=True,
        values=currencies,
        default='EUR')
