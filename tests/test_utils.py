import pytest
from src.utils import validate_data, calculate_totals

def test_validate_data_valid():
    data = {
        'seller_details': {
            'name': 'Seller Name',
            'address': 'Seller Address',
            'pan_no': 'PAN123',
            'gst_registration_no': 'GST123'
        },
        'billing_details': {
            'name': 'Billing Name',
            'address': 'Billing Address',
            'state_ut_code': 29
        },
        'shipping_details': {
            'name': 'Shipping Name',
            'address': 'Shipping Address',
            'state_ut_code': 29
        },
        'order_details': {
            'order_no': 'ORD123',
            'order_date': '2022-01-01'
        },
        'invoice_details': {
            'invoice_no': 'INV123',
            'invoice_date': '2022-01-01'
        },
        'items': [
            {
                'description': 'Item 1',
                'unit_price': 100,
                'quantity': 2,
                'tax_rate': 18
            }
        ]
    }
    validate_data(data)  # Should not raise any exceptions

def test_validate_data_missing_field():
    data = {
        'seller_details': {
            'name': 'Seller Name',
            'address': 'Seller Address',
            'pan_no': 'PAN123'
            # Missing gst_registration_no
        },
        'billing_details': {
            'name': 'Billing Name',
            'address': 'Billing Address',
            'state_ut_code': 29
        },
        'shipping_details': {
            'name': 'Shipping Name',
            'address': 'Shipping Address',
            'state_ut_code': 29
        },
        'order_details': {
            'order_no': 'ORD123',
            'order_date': '2022-01-01'
        },
        'invoice_details': {
            'invoice_no': 'INV123',
            'invoice_date': '2022-01-01'
        },
        'items': [
            {
                'description': 'Item 1',
                'unit_price': 100,
                'quantity': 2,
                'tax_rate': 18
            }
        ]
    }
    with pytest.raises(ValueError):
        validate_data(data)

def test_calculate_totals():
    items = [
        {
            'description': 'Item 1',
            'unit_price': 100,
            'quantity': 2,
            'discount': 10,
            'tax_rate': 18
        },
        {
            'description': 'Item 2',
            'unit_price': 200,
            'quantity': 1,
            'tax_rate': 18
        }
    ]
    place_of_supply = 'KARNATAKA'
    place_of_delivery = 'KARNATAKA'
    updated_items, total_amount = calculate_totals(items, place_of_supply, place_of_delivery)
    
    assert round(total_amount, 2) == 460.2  # (2*100-10)*1.18 + 200*1.18
    assert updated_items[0]['net_amount'] == 190
    assert round(updated_items[0]['tax_amount'], 2) == 34.2
    assert round(updated_items[0]['total_amount'], 2) == 224.2
    assert updated_items[1]['net_amount'] == 200
    assert round(updated_items[1]['tax_amount'], 2) == 36
    assert round(updated_items[1]['total_amount'], 2) == 236
