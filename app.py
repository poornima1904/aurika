from flask import Flask, request, render_template
from src.invoice_generator import generate_invoice

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if request.is_json:
        data = request.get_json()
        generate_invoice(data)
        return "Invoice generated successfully", 200
    else:
        return "Unsupported Media Type", 415

if __name__ == '__main__':
    app.run(debug=True)
