{
    'name': 'Tobako POS Receipt',
    'depends': [
        'base',
        'point_of_sale'
    ],
    'assets': {
        'point_of_sale.assets': [
            'tobako_pos_receipt/static/src/js/TobakoReceipt.js',
            'tobako_pos_receipt/static/src/js/TobakoReceiptStateButton.js',
            'tobako_pos_receipt/static/src/js/TobakoReprintReceiptStateButton.js',
            'tobako_pos_receipt/static/src/css/tobako-receipt.css'
        ],
        'web.assets_qweb': [
            'tobako_pos_receipt/static/src/xml/TobakoReceipt.xml',
            'tobako_pos_receipt/static/src/xml/TobakoReceiptStateButton.xml',
            'tobako_pos_receipt/static/src/xml/TobakoReprintReceiptStateButton.xml'
        ]
    }
}