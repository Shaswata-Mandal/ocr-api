from flask import Flask, request, jsonify
import easyocr
from PIL import Image
import io

app = Flask(__name__)
reader = easyocr.Reader(['en'])  # Create a reader for English language OCR

@app.route('/ocr', methods=['POST'])
def ocr():
    # Get the image file from the request
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))

    # Run OCR on the image
    result = reader.readtext(image)

    # Extract text from the OCR results
    detected_text = ' '.join([text[1] for text in result])

    # Return the detected text as a JSON response
    return jsonify({'text': detected_text})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
