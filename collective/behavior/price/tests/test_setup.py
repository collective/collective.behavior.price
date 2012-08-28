from Products.CMFCore.utils import getToolByName
from collective.behavior.price.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_collective_behavior_price_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(
            installer.isProductInstalled('collective.behavior.price'))

    def test_catalog__money(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.assertIn('money', catalog.schema())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile(
                'profile-collective.behavior.price:default'), u'0')

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.behavior.price'])
        self.failIf(installer.isProductInstalled('collective.behavior.price'))
