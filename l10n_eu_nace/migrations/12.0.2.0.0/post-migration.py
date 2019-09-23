# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api


def migrate(cr, registry):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        partners = env["res.partner"].search([("category_id", "!=", False)])
        for partner in partners:
            category = partner.category_id.filtered(
                lambda c: 'nace_' in c.get_external_id().get(c.id)
            )
            if not category:
                continue
            if len(category) > 1:
                category = category[0]
            partner.nace_id = env.ref(
                category.get_external_id().get(category.id).replace('old_', '')
            )
    cr.execute(
        """
        DELETE FROM res_partner_category
        WHERE id IN (
            SELECT res_id
            FROM ir_model_data
            WHERE name like 'old_nace_%'
        )
        """
    )
