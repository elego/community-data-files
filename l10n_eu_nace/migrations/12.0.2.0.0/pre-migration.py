# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def migrate(cr, version):
    cr.execute(
        """
        UPDATE ir_model_data
        SET name=concat('old_', name)
        WHERE name LIKE 'nace_%'
        AND module='l10n_eu_nace'
        """
    )
