# Replicate Web Demo

This is a minimal Flask application that allows you to upload an image, send it to the Replicate model `black-forest-labs/flux-kontext-pro`, and view the processed result directly in the browser.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python app.py
```

Open your browser at [http://localhost:5000](http://localhost:5000) to use the web interface.

## Providing the Replicate API token

Set the `REPLICATE_API_TOKEN` environment variable or create a file named
`.token` in the project root containing your token. If neither is provided, the
application uses a built-in token for backward compatibility.
