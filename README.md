# Flask Steganography Web Application

## Description
This project is a Flask-based web application that allows users to encode and decode secret messages within images using steganography. The application leverages the `Pillow` library for image processing, `stepic` for steganography, and `cryptography` for secure encryption and decryption of messages. The app is designed with a user-friendly web interface where users can upload images, input secret messages, and provide passwords for encryption and decryption.

## Features
- **Encode Messages**: Embed secret messages into images using a password for encryption.
- **Decode Messages**: Extract and decrypt messages from images using the provided password.
- **User-Friendly Interface**: Simple and intuitive web interface built with Flask.
- **Image Format Conversion**: Automatically converts images to PNG format during the encoding process to ensure compatibility.

## Technologies Used
- **Flask**: Web framework for the application.
- **Pillow**: Library for image processing.
- **stepic**: Library for steganography.
- **cryptography**: Library for encryption and decryption.
- **gunicorn**: WSGI HTTP Server for UNIX for running the app in production.

## Requirements
- Python 3.6+
- Flask
- Pillow
- stepic
- cryptography
- gunicorn

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/flask-steganography.git
    cd flask-steganography
    pip install -r requirements.txt
    python run.py
    ```

## Usage
**Navigate to the home page:**
Open your web browser and go to http://localhost:5000.

Encode a message:
1. Go to the "Encode" page.
2. Upload an image.
3. Enter the secret message and a password.
4. Download the encoded image.

Decode a message:
1. Go to the "Decode" page.
2. Upload the encoded image.
3. Enter the password used for encoding.
4. View the decoded message.

## Project Structure
```my_flask_app/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── encode.html
│   │   └── decode.html
│   └── static/
│       └── style.css
├── steganography/
│   ├── __init__.py
│   └── steg.py
├── uploads/
├── config.py
├── requirements.txt
└── run.py
```