{
    'name': 'Tobako POS Keymap',
    'version': '15.0.0.0',
    'category': 'Point of Sale',
    'sequence': -111,
    'summary': 'Keymap shortcut for faster POS transaction',
    'author': 'bidipeppercrap',
    'maintainer': 'bidipeppercrap',
    'website': 'https://www.bidipeppercrap.com',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'tobako_pos_keymap/static/src/js/PaymentButton.js',
            'tobako_pos_keymap/static/src/js/PaymentScreenKeymapped.js',
            'tobako_pos_keymap/static/src/js/ReceiptScreenKeymapped.js'
        ],
        'web.assets_qweb': [
            'tobako_pos_keymap/static/src/xml/PaymentButton.xml',
            'tobako_pos_keymap/static/src/xml/PaymentScreenKeymapped.xml',
            'tobako_pos_keymap/static/src/xml/ReceiptScreenKeymapped.xml'
        ]
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}