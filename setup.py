from setuptools import setup, find_packages

setup(
    name='invoice_generator',
    version='1.0.0',
    description='A tool to generate invoices for e-commerce orders',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Jinja2>=2.11.3',
        'pdfkit>=0.6.1',
        'num2words>=0.5.10',
        'pytest>=6.2.4'
    ],
    entry_points={
        'console_scripts': [
            'generate-invoice=main:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['templates/*.html', 'static/*.png'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
