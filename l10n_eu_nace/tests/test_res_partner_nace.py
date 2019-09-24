# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestResPartnerNace(TransactionCase):
    def setUp(self):
        super(TestResPartnerNace, self).setUp()
        self.nace = self.env['res.partner.nace'].create(
            {'name': 'name', 'code': 'code'}
        )

    def test_name_get(self):
        self.assertEqual(self.nace.name, 'name')
        self.assertEqual(self.nace.display_name, '[code] name')

    def test_name_search(self):
        self.assertEqual(
            self.nace.name_get(),
            self.env['res.partner.nace'].name_search('code'),
        )
