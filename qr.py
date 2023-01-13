import os
import qrcode
codes = input("Enter your code text: ")
img = qrcode.make(codes)
img.save('qr.png', 'PNG')
os.system('qr.png')
