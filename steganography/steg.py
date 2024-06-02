from PIL import Image
import stepic
from cryptography.fernet import Fernet
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode


def generate_key(password, salt=b'salt_'):
    # Use PBKDF2HMAC to derive a key from the password
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encode_message(image_path, message, password):
    try:
        # Convert the image to PNG format
        image = Image.open(image_path)
        png_image_path = os.path.splitext(image_path)[0] + "_temp.png"
        image.save(png_image_path, 'PNG')

        key = generate_key(password)
        cipher_suite = Fernet(key)
        encrypted_message = cipher_suite.encrypt(message.encode())
        image = Image.open(png_image_path)
        encoded_image = stepic.encode(image, encrypted_message)
        encoded_image_path = os.path.splitext(image_path)[0] + "_encoded.png"
        encoded_image.save(encoded_image_path, 'PNG')

        # Remove the temporary PNG image
        os.remove(png_image_path)

        return encoded_image_path
    except Exception as e:
        print(f"Encoding error: {e}")
        raise

def decode_message(image_path, password):
    try:
        key = generate_key(password)
        cipher_suite = Fernet(key)
        image = Image.open(image_path)
        encrypted_message = stepic.decode(image)
        decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
        return decrypted_message
    except Exception as e:
        print(f"Decoding error: {e}")
        raise
