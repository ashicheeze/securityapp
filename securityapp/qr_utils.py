import base64
from io import BytesIO

try:
    import qrcode
except ImportError:  # pragma: no cover - library may not be installed
    qrcode = None


def generate_qr(user_id: str) -> str:
    """Generate a base64-encoded PNG QR code for the provided user id.

    If the `qrcode` library is not available, a ValueError is raised.
    """
    if qrcode is None:
        raise ValueError("qrcode library is not installed")

    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(user_id)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")
