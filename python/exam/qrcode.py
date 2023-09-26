import pyqrcode
import png

link = "https://www.facebook.com/profile.php?id=100012080236909"

qr_code = pyqrcode.create(link)
qr_code.png("facebook.png", scale=5)

