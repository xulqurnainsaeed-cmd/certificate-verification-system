import qrcode

# CERTIFICATE REFERENCE
reference = "8D6R-02ZA-81UD"

# LIVE WEBSITE URL
base_url = "https://certificate-verification-system-ssvl.onrender.com"

# FULL VERIFICATION URL
verification_url = f"{base_url}/verify/{reference}"

# GENERATE QR
img = qrcode.make(verification_url)

# SAVE QR IMAGE
img.save(f"static/qr_codes/{reference}.png")

print("QR Code Generated Successfully")