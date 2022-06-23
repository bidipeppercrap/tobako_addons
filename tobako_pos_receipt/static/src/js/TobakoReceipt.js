odoo.define('tobako_pos_receipt.TobakoReceipt', function (require) {
    'use strict'

    const OrderReceipt = require('point_of_sale.OrderReceipt')

    OrderReceipt.template = 'TobakoReceipt'
})