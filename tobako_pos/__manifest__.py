{
    'name': 'POS Simplified',
    'version': '1.0',
    'summary': 'POS Simplified for Retail',
    'application': False,
    'description': """
Simplify the POS by removing fields that is unnecessary for a retail industry.
    """,
    'author': 'bidipeppercrap',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_setting.xml',
        # 'views/pos_config.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            # '/tobako_pos/static/src/css/style.css',
            '/tobako_pos/static/src/css/override-style.css'
        ]
    },
    'qweb': ['static/src/xml/pos_receipt.xml']
}