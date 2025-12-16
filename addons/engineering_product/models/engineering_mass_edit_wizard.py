from odoo import models, fields, api

class EngineeringMassEditWizard(models.TransientModel):
    _name = 'engineering.mass.edit.wizard'
    _description = 'Mass Assign Engineering Attributes'

    # User inputs (all optional)
    part_type = fields.Char()
    tolerance = fields.Char()
    power_rating = fields.Char()
    voltage_rating = fields.Char()

    def action_apply(self):
        products = self.env['product.template'].browse(
            self.env.context.get('active_ids', [])
        )

        vals = {}
        for field in [
            'part_type',
            'tolerance',
            'power_rating',
            'voltage_rating',
        ]:
            value = getattr(self, field)
            if value:
                vals[field] = value

        if vals:
            products.write(vals)

        return {'type': 'ir.actions.act_window_close'}
