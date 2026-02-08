import qrcode
import os

print("==== QR Code Generator ====")

data = input("Enter text or URL: ")
file_name = input("Enter file name (without extension): ")

# create output folder if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"output/{file_name}.png")

print(f"QR Code saved successfully in output/{file_name}.png")
