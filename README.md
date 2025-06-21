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
By default the server listens on port `5000`. You can change the port by setting
the `PORT` environment variable:

```bash
PORT=5001 python app.py
```

Open your browser at [http://localhost:5000](http://localhost:5000) (or your chosen port) to use the web interface.
