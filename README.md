# Invoice Generator

This project generates an invoice for orders placed on an e-commerce platform. The invoice format and structure match the provided example.

## Features

- Generate PDF invoices based on order data
- Supports itemized billing with taxes and discounts
- Configurable seller, billing, and shipping details
- Detailed error handling and validation
- Continuous Integration setup with GitHub Actions

## Requirements

- Python 3.x
- `wkhtmltopdf`

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/invoice-generator.git
    cd invoice-generator
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install `wkhtmltopdf`**:
    - On Ubuntu:
        ```bash
        sudo apt-get update
        sudo apt-get install -y xfonts-75dpi xfonts-base
        wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
        sudo dpkg -i wkhtmltox_0.12.6-1.bionic_amd64.deb || sudo apt-get -f install -y
        sudo cp /usr/local/bin/wkhtmltopdf /usr/bin
        sudo cp /usr/local/bin/wkhtmltoimage /usr/bin
        ```

## Usage

1. **Modify the `data` dictionary in `main.py`** with the necessary details.

2. **Run the script**:
    ```bash
    python main.py
    ```

3. The generated invoice will be saved as `invoice.pdf` in the current directory.

## Project Structure

- `templates/`: Contains the HTML template for the invoice.
- `static/`: Contains static files like the company logo and signature.
- `src/`: Contains the main logic for generating the invoice and utility functions.
- `tests/`: Contains unit tests for the project.
- `.github/workflows/`: Contains the GitHub Actions CI workflow.
- `main.py`: Entry point of the application.
- `requirements.txt`: List of dependencies.
- `README.md`: Documentation about the project.

## Running Tests

1. **Run the tests**:
    ```bash
    pytest
    ```

## Continuous Integration

The project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/ci.yml`.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-branch
    ```
3. **Make your changes**.
4. **Commit your changes**:
    ```bash
    git commit -m "Description of changes"
    ```
5. **Push to the branch**:
    ```bash
    git push origin feature-branch
    ```
6. **Create a pull request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
