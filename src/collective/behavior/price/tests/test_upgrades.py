from collective.behavior.price.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    @mock.patch('collective.behavior.price.upgrades.getToolByName')
    def test_reimport_catalog(self, getToolByName):
        from collective.behavior.price.upgrades import reimport_catalog
        reimport_catalog(self.portal)
        PROFILE_ID = 'profile-collective.behavior.price:default'
        getToolByName().runImportStepFromProfile.assert_called_with(PROFILE_ID, 'catalog', run_dependencies=False, purge_old=False)
        self.assertTrue(getToolByName().clearFindAndRebuild.called)
