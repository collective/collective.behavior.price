from collective.behavior.price import _
from plone.supermodel.model import Schema
from zope import schema


class PriceSchema(Schema):
    """Schema for behavior: Price"""

    price = schema.Decimal(
        title=_(u"Price"),
        required=True)
