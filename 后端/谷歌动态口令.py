import hmac
import base64
import struct
import hashlib
import time
from MyQR import myqr
from django.http import HttpResponse


def cal_google_code(secret_key):
    """计算谷歌验证码　TOTP"""
    duration_input = int(time.time())//30
    key = base64.b32decode(secret_key)  # length of the key must be a multiplier of eight
    msg = struct.pack(">q", duration_input)
    google_code = hmac.new(key, msg, hashlib.sha1).digest()
    o = google_code[19] & 15
    google_code = str((struct.unpack(">i", google_code[o:o+4])[0] & 0x7fffffff) % 1000000)
    if len(google_code) == 5:  # only if length of the code is 5, a zero will be added at the beginning of the code.
        google_code = '0' + google_code
        print(google_code)
    return google_code


def get_qrcode():
    """生成二维码"""
    sec = pyotp.random_base32()
    qr_uri = pyotp.totp.TOTP(sec).provisioning_uri('test')
    img = myqr.run(words=qr_uri, save_name='code.png')
    return HttpResponse(img)



import pyotp
# 生成谷歌动态口令并验证
def qqq(request):
    sec = pyotp.random_base32()
    qr_uri = pyotp.totp.TOTP(sec).provisioning_uri('test')
    img = myqr.run(words=qr_uri, save_name='code.png')
    return HttpResponse(img, content_type='image/png')

def verify(request):
    """验证动态口令"""
    totp = pyotp.TOTP('YLMZFYYJDYTLZOKE').now()
    code = request.GET.get('code')
    if code == totp:
        return True
    else:
        return False
