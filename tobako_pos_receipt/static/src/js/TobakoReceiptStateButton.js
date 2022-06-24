odoo.define('tobako_pos_receipt.TobakoReceiptStateButton', function (require) {
    'use strict'

    const ReceiptScreen = require('point_of_sale.ReceiptScreen')
    const Registries = require('point_of_sale.Registries')

    const TobakoReceiptStateButton = (ReceiptScreen) => class extends ReceiptScreen {
        constructor() {
            super(...arguments)
        }

        changeState() {
            const receiptState = this.orderReceipt.el.getElementsByClassName('tobako-pos-receipt__text--copy')[0]
            const currentState = receiptState.innerHTML
            const states = ['normal', '*** COPY ***', '*** ASLI ***']
            const currentStateIndex = states.indexOf(currentState)
            const stateIndex = (currentStateIndex + 1) < states.length ? currentStateIndex + 1 : 0
            const state = states[stateIndex]

            if (stateIndex == 0) receiptState.classList.add('tobako-pos-receipt__hide')
            else receiptState.classList.remove('tobako-pos-receipt__hide')
            receiptState.innerHTML = state
        }
    }

    Registries.Component.extend(ReceiptScreen, TobakoReceiptStateButton)

    return TobakoReceiptStateButton
})
