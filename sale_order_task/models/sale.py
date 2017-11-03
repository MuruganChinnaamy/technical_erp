# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from datetime import datetime, timedelta
from openerp import SUPERUSER_ID
from openerp import api, fields, models, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError
from openerp.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
import copy

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ['sale.order']
    _description = "Sales Order"
    
    copy_line = fields.One2many('copy.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True)
    
    
    
    
    
    
class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = ['sale.order.line']
    
    @api.multi
    def write(self,vals):
        #first model
        copy_data_list = []
        print self.order_id
        
        copy_order = self.env['copy.order.line'].search([('order_id','=',self.order_id.id)])
        orig_sale_line = self
        
        res = {

            'order_id': self.order_id.id,

            'product_id': orig_sale_line.product_id.id,

            'name': orig_sale_line.name,

            'sequence': orig_sale_line.sequence,

            'price_unit': orig_sale_line.price_unit,

            'product_uom': orig_sale_line.product_uom.id,

            'product_uom_qty': orig_sale_line.product_uom_qty or 0,

            

        }
        if copy_order:
            self.env['copy.order.line'].write(res)
        else:

            self.env['copy.order.line'].create(res)
           

        return True
      
    
    
class CopyOrderLine(models.Model):
    _name = 'copy.order.line'
    _inherit = ['sale.order.line']
    
    order_id = fields.Many2one('sale.order', string='Order Reference', required=True, index=True, copy=False)
    name = fields.Text(string='Description', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
 
    invoice_lines = fields.Many2many('account.invoice.line', 'sale_order_line_invoice_rel', 'order_line_id', 'invoice_line_id', string='Invoice Lines', copy=False)
    invoice_status = fields.Selection([
        ('upselling', 'Upselling Opportunity'),
        ('invoiced', 'Fully Invoiced'),
        ('to invoice', 'To Invoice'),
        ('no', 'Nothing to Invoice')
        ], string='Invoice Status', compute='_compute_invoice_status', store=True, readonly=True, default='no')
    price_unit = fields.Float('Unit Price', required=True, digits=dp.get_precision('Product Price'), default=0.0)
 
    price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', readonly=True, store=True)
    price_tax = fields.Monetary(compute='_compute_amount', string='Taxes', readonly=True, store=True)
    price_total = fields.Monetary(compute='_compute_amount', string='Total', readonly=True, store=True)
 
    price_reduce = fields.Monetary(compute='_get_price_reduce', string='Price Reduce', readonly=True, store=True)
    tax_id = fields.Many2many('account.tax', string='Taxes')
 
    discount = fields.Float(string='Discount (%)', digits=dp.get_precision('Discount'), default=0.0)
 
    product_id = fields.Many2one('product.product', string='Product', domain=[('sale_ok', '=', True)], change_default=True, ondelete='restrict', required=True)
    product_uom_qty = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'), required=True, default=1.0)
    product_uom = fields.Many2one('product.uom', string='Unit of Measure', required=True)
 
    qty_delivered_updateable = fields.Boolean(compute='_compute_qty_delivered_updateable', string='Can Edit Delivered', readonly=True, default=True)
    qty_delivered = fields.Float(string='Delivered', copy=False, digits=dp.get_precision('Product Unit of Measure'), default=0.0)
    qty_to_invoice = fields.Float(
        compute='_get_to_invoice_qty', string='To Invoice', store=True, readonly=True,
        digits=dp.get_precision('Product Unit of Measure'), default=0.0)
    qty_invoiced = fields.Float(
        compute='_get_invoice_qty', string='Invoiced', store=True, readonly=True,
        digits=dp.get_precision('Product Unit of Measure'), default=0.0)
 
    salesman_id = fields.Many2one(related='order_id.user_id', store=True, string='Salesperson', readonly=True)
    currency_id = fields.Many2one(related='order_id.currency_id', store=True, string='Currency', readonly=True)
    company_id = fields.Many2one(related='order_id.company_id', string='Company', store=True, readonly=True)
    order_partner_id = fields.Many2one(related='order_id.partner_id', store=True, string='Customer')
 
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sale Order'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], related='order_id.state', string='Order Status', readonly=True, copy=False, store=True, default='draft')
 
    customer_lead = fields.Float(
        'Delivery Lead Time', required=True, default=0.0,
        help="Number of days between the order confirmation and the shipping of the products to the customer", oldname="delay")
    procurement_ids = fields.One2many('procurement.order', 'sale_line_id', string='Procurements')