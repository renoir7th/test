import os
import io
import base64
from flask import Flask, render_template, request, jsonify
from PIL import Image
import requests
import replicate

app = Flask(__name__)

# Load Replicate API token from environment or .token file
token = os.environ.get("REPLICATE_API_TOKEN")
if not token:
    token_path = ".token"
    if os.path.exists(token_path):
        with open(token_path) as f:
            token = f.read().strip()
if not token:
    # Fallback to previous hard-coded token for backward compatibility
    token = "r8_aLads83FscsbQT8nvQtLhdFYiP3qbnf3EzRZ1"
os.environ["REPLICATE_API_TOKEN"] = token

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_image():
    file = request.files.get("image")
    prompt = request.form.get("prompt", "Make this a 90s cartoon")
    if not file:
        return jsonify({"error": "No image uploaded"}), 400

    # Resize image to reduce payload
    image = Image.open(file.stream)
    image.thumbnail((512, 512))
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)

    output = replicate.run(
        "black-forest-labs/flux-kontext-pro",
        input={
            "prompt": prompt,
            "input_image": buffer,
            "output_format": "jpg"
        }
    )

    if isinstance(output, list):
        image_url = output[0]
    else:
        image_url = output

    resp = requests.get(image_url)
    if resp.status_code != 200:
        return jsonify({"error": "Failed to fetch output"}), 500

    encoded = base64.b64encode(resp.content).decode("utf-8")
    return jsonify({"image": encoded})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
