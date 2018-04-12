import qrcode
from PIL import Image

def url(url):
    #生成二维码
    img = qrcode.make(url)
    path = 'static/qrimg/1.png'
    img.save(path)
    return path
