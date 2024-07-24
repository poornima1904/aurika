def validate_data(data):
    # Add validation logic here
    required_fields = ['seller_details', 'billing_details', 'shipping_details', 'order_details', 'invoice_details', 'items']
    
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    
    # Validate seller details
    seller_fields = ['name', 'address', 'pan_no', 'gst_registration_no']
    for field in seller_fields:
        if field not in data['seller_details']:
            raise ValueError(f"Missing required field in seller details: {field}")

    # Validate billing details
    billing_fields = ['name', 'address', 'state_ut_code']
    for field in billing_fields:
        if field not in data['billing_details']:
            raise ValueError(f"Missing required field in billing details: {field}")

    # Validate shipping details
    shipping_fields = ['name', 'address', 'state_ut_code']
    for field in shipping_fields:
        if field not in data['shipping_details']:
            raise ValueError(f"Missing required field in shipping details: {field}")

    # Validate order details
    order_fields = ['order_no', 'order_date']
    for field in order_fields:
        if field not in data['order_details']:
            raise ValueError(f"Missing required field in order details: {field}")

    # Validate invoice details
    invoice_fields = ['invoice_no', 'invoice_date']
    for field in invoice_fields:
        if field not in data['invoice_details']:
            raise ValueError(f"Missing required field in invoice details: {field}")

    # Validate items
    if not data['items'] or not isinstance(data['items'], list):
        raise ValueError("Items must be a non-empty list")
    for item in data['items']:
        item_fields = ['description', 'unit_price', 'quantity', 'tax_rate']
        for field in item_fields:
            if field not in item:
                raise ValueError(f"Missing required field in item: {field}")

def calculate_totals(items, place_of_supply, place_of_delivery):
    total_amount = 0
    for item in items:
        item['net_amount'] = item['unit_price'] * item['quantity'] - item.get('discount', 0)
        if place_of_supply == place_of_delivery:
            item['tax_type'] = 'CGST/SGST'
            item['cgst'] = round(item['net_amount'] * 0.09, 2)
            item['sgst'] = round(item['net_amount'] * 0.09, 2)
            item['tax_amount'] = item['cgst'] + item['sgst']
        else:
            item['tax_type'] = 'IGST'
            item['igst'] = round(item['net_amount'] * 0.18, 2)
            item['tax_amount'] = item['igst']
        item['total_amount'] = item['net_amount'] + item['tax_amount']
        total_amount += item['total_amount']
    return items, total_amount


