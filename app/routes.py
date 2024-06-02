from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
from steganography.steg import encode_message, decode_message

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/encode', methods=['GET', 'POST'])
    def encode():
        if request.method == 'POST':
            file = request.files['image']
            message = request.form['message']
            password = request.form['password']
            print("Received file for encoding:", file.filename)
            print("Received message:", message)
            print("Received password:", password)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                folder_path = app.config['UPLOAD_FOLDER']
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                filepath = os.path.join(folder_path, filename)
                file.save(filepath)
                print("File saved at:", filepath)
                try:
                    encoded_image_path = encode_message(filepath, message, password)
                    print("Encoded image saved at:", encoded_image_path)
                    return send_from_directory(directory=os.path.dirname(encoded_image_path), filename=os.path.basename(encoded_image_path), as_attachment=True)
                except Exception as e:
                    flash(f"Error: {e}", 'danger')
                    print("Encoding error:", e)
            else:
                flash('Invalid file type', 'danger')
                print("Invalid file type:", file.filename)
        return render_template('encode.html')

    @app.route('/decode', methods=['GET', 'POST'])
    def decode():
        message = None
        if request.method == 'POST':
            file = request.files['image']
            password = request.form['password']
            print("Received file for decoding:", file.filename)
            print("Received password:", password)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                print("File saved at:", filepath)
                try:
                    message = decode_message(filepath, password)
                    print("Decoded message:", message)
                    flash(f"Decoded message: {message}", 'success')
                except ValueError as ve:
                    flash(f"Error: {ve}", 'danger')
                    print("Decoding error:", ve)
                except Exception as e:
                    flash(f"Unexpected error: {e}", 'danger')
                    print("Unexpected decoding error:", e)
            else:
                flash('Invalid file type', 'danger')
                print("Invalid file type:", file.filename)
        return render_template('decode.html', message=message)
