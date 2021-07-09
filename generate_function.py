#----------------------------------------------------------------------------------------------------------------------------
# Imports
from pyqrcode import QRCode
import pyqrcode
import png
from io import BytesIO
import base64
from PIL import Image
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Generate QR Code with content
def generate_qr(content, size):
	qr = pyqrcode.create(content)
	qr_image = './assets/QR.png'
	with open(qr_image, 'wb') as qr_file:
		qr.png(qr_file, scale=size)

	qr_code = Image.open(qr_image)
	return qr_code
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# QR Code Image Download Link
def image_download(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}" download="qr.jpg">Download QR Code as .jpg</a>'
    return href
#----------------------------------------------------------------------------------------------------------------------------