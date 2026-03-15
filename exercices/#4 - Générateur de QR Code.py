#4 - Générateur de QR Code
import qrcode

url = input(" Enter the URL: ").strip()
file_path = "C:\\Users\\bally\\Documents\\PYTHON\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)
qr.make

img = qr.make_image()
img.save(file_path)

print("QR Code was generated!")  