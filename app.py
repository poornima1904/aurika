from flask import Flask, request, render_template
from src.invoice_generator import generate_invoice

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = {
        'description': request.form.get('description'),
        'unit_price': float(request.form.get('unit_price')),
        'quantity': int(request.form.get('quantity')),
        'discount': float(request.form.get('discount')),
        'tax_rate': float(request.form.get('tax_rate'))
    }
    generate_invoice(data)
    return "Invoice generated successfully", 200

if __name__ == '__main__':
    app.run(debug=True)
