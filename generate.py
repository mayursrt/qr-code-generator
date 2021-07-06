#----------------------------------------------------------------------------------------------------------------------------
# Imports
import streamlit as st
from pyqrcode import QRCode
import pyqrcode
from PIL import Image
import png
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