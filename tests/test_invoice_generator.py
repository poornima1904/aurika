import os
import pytest
from src.invoice_generator import generate_invoice

def test_generate_invoice_valid():
    data = {
        'seller_details': {
            'name': 'Varasidihi Silk Exports',
            'address': '75, 3rd Cross, Lalbagh Road, BENGALURU, KARNATAKA, 560027',
            'pan_no': 'AACFV3325K',
            'gst_registration_no': '29AACFV3325K1ZY'
        },
        'place_of_supply': 'KARNATAKA',
        'billing_details': {
            'name': 'Madhu B',
            'address': 'Eurofins IT Solutions India Pvt Ltd., 1st Floor, Maruti Platinum, Lakshminarayana Pura, AECS Layout, BENGALURU, KARNATAKA, 560037',
            'state_ut_code': 29
        },
        'shipping_details': {
            'name': 'Madhu B',
            'address': 'Eurofins IT Solutions India Pvt Ltd., 1st Floor, Maruti Platinum, Lakshminarayana Pura, AECS Layout, BENGALURU, KARNATAKA, 560037',
            'state_ut_code': 29
        },
        'place_of_delivery': 'KARNATAKA',
        'order_details': {
            'order_no': '403-3225714-7676307',
            'order_date': '28.10.2019'
        },
        'invoice_details': {
            'invoice_no': 'IN-761',
            'invoice_date': '28.10.2019'
        },
        'reverse_charge': 'No',
        'items': [
            {
                'description': 'Varasidihi Silks Men\'s Formal Shirt (SH-05-42, Navy Blue, 42)',
                'unit_price': 500.00,
                'quantity': 1,
                'discount': 0,
                'tax_rate': 18
            },
            {
                'description': 'Varasidihi Silks Men\'s Formal Shirt (SH-05-40, Navy Blue, 40)',
                'unit_price': 500.00,
                'quantity': 1,
                'discount': 0,
                'tax_rate': 18
            }
        ]
    }

    try:
        generate_invoice(data)
        assert os.path.exists('invoice.pdf')
    finally:
        if os.path.exists('invoice.pdf'):
            os.remove('invoice.pdf')

def test_generate_invoice_invalid():
    data = {
        'seller_details': {
            'name': 'Varasidihi Silk Exports',
            'address': '75, 3rd Cross, Lalbagh Road, BENGALURU, KARNATAKA, 560027',
            'pan_no': 'AACFV3325K'
            # Missing gst_registration_no
        },
        'place_of_supply': 'KARNATAKA',
        'billing_details': {
            'name': 'Madhu B',
            'address': 'Eurofins IT Solutions India Pvt Ltd., 1st Floor, Maruti Platinum, Lakshminarayana Pura, AECS Layout, BENGALURU, KARNATAKA, 560037',
            'state_ut_code': 29
        },
        'shipping_details': {
            'name': 'Madhu B',
            'address': 'Eurofins IT Solutions India Pvt Ltd., 1st Floor, Maruti Platinum, Lakshminarayana Pura, AECS Layout, BENGALURU, KARNATAKA, 560037',
            'state_ut_code': 29
        },
        'place_of_delivery': 'KARNATAKA',
        'order_details': {
            'order_no': '403-3225714-7676307',
            'order_date': '28.10.2019'
        },
        'invoice_details': {
            'invoice_no': 'IN-761',
            'invoice_date': '28.10.2019'
        },
        'reverse_charge': 'No',
        'items': [
            {
                'description': 'Varasidihi Silks Men\'s Formal Shirt (SH-05-42, Navy Blue, 42)',
                'unit_price': 500.00,
                'quantity': 1,
                'discount': 0,
                'tax_rate': 18
            },
            {
                'description': 'Varasidihi Silks Men\'s Formal Shirt (SH-05-40, Navy Blue, 40)',
                'unit_price': 500.00,
                'quantity': 1,
                'discount': 0,
                'tax_rate': 18
            }
        ]
    }

    with pytest.raises(ValueError):
        generate_invoice(data)
