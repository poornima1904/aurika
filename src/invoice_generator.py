import pdfkit
from jinja2 import Environment, FileSystemLoader
from num2words import num2words
import os
from .utils import validate_data, calculate_totals

def generate_invoice(data):
    try:
        # Validate input data
        validate_data(data)

        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('invoice_template.html')

        # Compute derived values
        items, total_amount = calculate_totals(data['items'], data['place_of_supply'], data['place_of_delivery'])
        amount_in_words = num2words(total_amount).title() + ' Only'

        html_out = template.render(
            logo=os.path.join('static', 'logo.png'),
            signature=os.path.join('static', 'signature.png'),
            seller_details=data['seller_details'],
            billing_details=data['billing_details'],
            shipping_details=data['shipping_details'],
            order_details=data['order_details'],
            invoice_details=data['invoice_details'],
            reverse_charge=data['reverse_charge'],
            items=items,
            total_amount=total_amount,
            amount_in_words=amount_in_words,
            seller_name=data['seller_details']['name']
        )

        path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'  # Update this path if needed
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        options = {
            'enable-local-file-access': None  # Allow access to local files
        }
        pdfkit.from_string(html_out, 'invoice.pdf', configuration=config, options=options)
        print("Invoice generated successfully.")
    except ValueError as ve:
        print(f"Validation error: {ve}")
        raise  # Re-raise the ValueError
    except Exception as e:
        print(f"An error occurred: {e}")
