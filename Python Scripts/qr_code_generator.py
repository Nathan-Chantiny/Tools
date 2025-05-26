'''
Little script for generating QR codes
'''

import pyqrcode
import png
from pyqrcode import QRCode

# String that represents the QR code
s = "[INSERT URL STRING HERE]"

# Genereate QR code
url = pyqrcode.create(s)

# Export QR code as SVG
url.svg("d:\PROJECTS\Tools\QR_Codes\[NAME OF FILE HERE].svg", scale=8)

# Export QR code as PNG
url.png("d:\PROJECTS\Tools\QR_Codes\[NAME OF FILE HERE].png", scale=6)

# Print done after file is done being exported
print("done")