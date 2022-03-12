{
    'name': 'Product Form Simplified',
    'version': '1.0',
    'summary': 'Product Form Simplified for Retails',
    'application': True,
    'description': """
Simplify the Product form by removing fields that is unnecessary for a retail industry.
    """,
    'author': 'bidipeppercrap',
    'depends': ['point_of_sale'],
    'data': [
        'views/product_create_form.xml',
        'views/product_create_action.xml',
        'views/product_views.xml',
    ]
}