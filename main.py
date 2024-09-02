import qrcode
from PIL import Image

logo_link = 'LOGOIMAGE.jpg' # your image 

logo = Image.open(logo_link)


logo = logo.convert("RGBA")

basewidth = 100

# Calculate the height using the same aspect ratio
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))

# Resize the logo using LANCZOS filter
logo = logo.resize((basewidth, hsize), Image.LANCZOS)

# Create the QR Code object with high error correction
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

url = 'https://github.com/396Kv'  # Replace with your URL

QRcode.add_data(url)
QRcode.make()

# Generate the QR code image
QRimg = QRcode.make_image(fill_color="black", back_color="white").convert('RGB')

pos = (
    (QRimg.size[0] - logo.size[0]) // 2,
    (QRimg.size[1] - logo.size[1]) // 2
)

logo_mask = logo.split()[3]
QRimg.paste(logo, pos, mask=logo_mask)
QRimg.save('custom_qrcode.png')
