from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    amount_tariff = fields.Monetary(
        string='Tariff Charges', 
        store=True, 
        readonly=True, 
        compute='_amount_all'
    )

    @api.depends('order_line.price_subtotal', 'order_line.tariff_rate')
    def _amount_all(self):
        # 1. Run the standard Odoo total calculations first
        super(PurchaseOrder, self)._amount_all()
        
        for order in self:
            tariff_sum = 0.0
            for line in order.order_line:
                # We use getattr to safely check for the field during initial installation
                rate = getattr(line, 'tariff_rate', 0.0) or 0.0
                tariff_sum += (line.price_subtotal * (rate / 100.0))
            
            order.amount_tariff = tariff_sum
            order.amount_total += tariff_sum

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    # This field MUST be defined here so the logic above can see it
    tariff_rate = fields.Float(
        string="Tariff Rate (%)", 
        related='product_id.tariff_rate', 
        readonly=True, 
        store=True
    )