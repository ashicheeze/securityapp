# SecurityApp

This repository contains a very small Flask application that demonstrates generating QR
codes and storing a simple purchase history. It was originally created as a toy example
for QR code functionality. The application is not meant for production use.

## Project layout

```
securityapp/       Python package with the Flask application
  ├── app.py       – Flask routes for QR code and purchase logging
  ├── qr_utils.py  – Helper to generate a base64 encoded QR code
app/
  ├── index.html   – Example page showing a placeholder QR image
  └── qr_placeholder.svg – Pre-generated SVG used by the page
```

Purchase data is stored in `purchases.json` in the project root whenever the `/purchase`
endpoint is called.

## Running the application

1. Install dependencies (Flask and qrcode):
   ```bash
   pip install flask qrcode[pil]
   ```
2. Start the server:
   ```bash
   python -m securityapp.app
   ```
   The server will listen on <http://localhost:5000>.

## API endpoints

- `GET /qr/<user_id>` – returns JSON containing a base64 PNG QR code for the provided
  `user_id`.
- `POST /purchase` – accepts JSON `{"user_id": "...", "item": "..."}` and appends the
  purchase to `purchases.json`.

## Placeholder web page

Open `app/index.html` in a browser to view a simple page that displays a placeholder QR
code. The code was generated using `app/generate_placeholder_qr_svg.py`.

## License

No license has been provided; see repository history for details.
