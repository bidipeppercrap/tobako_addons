odoo.define('tobako_pos_receipt.models', function (require) {
    'use strict'

    const models = require('point_of_sale.models')
    const OrderSuper = models.Order

    models.Order = models.Order.extend({
        export_for_printing: function () {
            var receipt = OrderSuper.prototype.export_for_printing.call(this)

            receipt.state = 'normal'

            return receipt
        }
    })
})