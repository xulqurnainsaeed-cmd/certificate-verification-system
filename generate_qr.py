import qrcode

# CERTIFICATE REFERENCE
reference = "YOKME2KHUNOA6C5TTK-101647"

# LIVE WEBSITE URL
base_url = "https://www.turkiye-edu.com"

# FULL VERIFICATION URL
verification_url = f"{base_url}/verify/{reference}"

# GENERATE QR
img = qrcode.make(verification_url)

# SAVE QR IMAGE
img.save(f"static/qr_codes/{reference}.png")

print("QR Code Generated Successfully")