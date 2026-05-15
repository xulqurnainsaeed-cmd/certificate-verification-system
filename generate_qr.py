import qrcode

reference = "CERT-001"

url = f"http://127.0.0.1:5000/verify/{reference}"

img = qrcode.make(url)

img.save(f"static/qr_codes/{reference}.png")

print("QR Code Generated Successfully")