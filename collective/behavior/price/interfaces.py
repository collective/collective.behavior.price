from collective.behavior.price import _
from moneyed.classes import CURRENCIES
from plone.directives import form
from zope.interface import Attribute
from zope.interface import Interface
from zope.schema import Choice
from zope.schema import Decimal


class IPrice(form.Schema):
    """Add salable field to dexterity type.
    """

    price = Decimal(
            title=_(u"Price"),
            required=True)

    currency = Attribute('Currency like EUR')
    money = Attribute('Money instance')


currencies = CURRENCIES.keys()
currencies.sort()


class ICurrency(Interface):

    default_currency = Choice(
        title=_(u'Default Currency'),
        description=_(u'Default Currency for price field.'),
        required=True,
        values=currencies,
        default='EUR')
