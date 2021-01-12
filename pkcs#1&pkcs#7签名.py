import hashlib
import binascii
import sys
import rsa
import base64
from OpenSSL import crypto
from OpenSSL.crypto import load_certificate, load_privatekey

def get_digest_value():
    # ******** sha1摘要算法 ********
    with open('/home/user/Desktop/VCP_FOREX_SDJ_20210108_0001.txt') as f:
        data = f.read()
    # 签名内容生成摘要： sha1, base64
    if not isinstance(data, bytes):
        data = str(data).encode('utf-8')
    sha = hashlib.sha1(data).hexdigest()
    # print(sys.getsizeof(sha))
    # print(len(sha))
    print(sha)



    # ******** pkcs#1签名 ********
    # with open('/home/user/Desktop/pri.key', 'rb') as privatefile:
        #私钥的绝对路径
        # keydata = privatefile.read()
    # privatekey = rsa.PrivateKey.load_pkcs1(keydata)
    # signature = rsa.sign(sha.encode('utf-8'), privatekey, 'SHA-1')
    # sign = base64.b64encode(signature).decode('utf-8')
    # print(len(sign)) 
    # return sign



    # ******** pkcs#7签名 一 ********
    with open('/home/user/Desktop/test.pfx', 'rb') as f:
        pfx_buffer = f.read()
    p12 = crypto.load_pkcs12(pfx_buffer, '123456')
    signcert = p12.get_certificate()
    pkey = p12.get_privatekey()
    bio_in = crypto._new_mem_buf()

    PKCS7_TEXT = 0x1
    PKCS7_NOSIGS = 0x4
    PKCS7_DETACHED = 0x40
    PKCS7_NOATTR = 0x100
    PKCS7_NOSMIMECAP = 0x200
    PKCS7_PARTIAL = 0x4000

    # 默认使用SHA256算法，暂未找到方法切换到SHA1
    pkcs7 = crypto._lib.PKCS7_sign(signcert._x509, pkey._pkey, crypto._ffi.NULL, bio_in, PKCS7_DETACHED|PKCS7_NOATTR)
    bio_out = crypto._new_mem_buf()
    crypto._lib.i2d_PKCS7_bio(bio_out, pkcs7)
    sigbytes = crypto._bio_to_string(bio_out)
    sigb64 = base64.b64encode(sigbytes)
    print(sigb64)

    with open(r'./sign_logon_bin.p7b', 'wb') as f:
        f.write(sigbytes)

    SignedData = base64.urlsafe_b64encode(sigbytes)
    # SignedData = base64.b64encode(sigbytes)
    # print("SignedData = ", SignedData)

    with open(r'./sign_logon_b64.p7b', 'wb') as f:
        f.write(sigbytes)
    return SignedData



    # ******** pkcs#7签名 二 ********
    # try:
    #     p12 = crypto.load_pkcs12(open("/home/user/Desktop/test.pfx", 'rb').read(), "123456")
    #     # print("p12 : ", p12)
    #     signcert = p12.get_certificate()
    #     pkey = p12.get_privatekey()

    #     text = "This is the text to be signed"
    #     bio_in = crypto._new_mem_buf(sha.encode())
    #     PKCS7_NOSIGS = 0x4
    #     pkcs7 = crypto._lib.PKCS7_sign(signcert._x509, pkey._pkey, crypto._ffi.NULL, bio_in, PKCS7_NOSIGS)
    #     bio_out = crypto._new_mem_buf()
    #     crypto._lib.i2d_PKCS7_bio(bio_out, pkcs7)

    #     sigbytes = crypto._bio_to_string(bio_out)

    #     signed_data = base64.b64encode(sigbytes)
    #     return signed_data
    # except Exception as err:
    #     print("Exception happens in sign_data and error is: ", err)
    #     return 0, str(err)


print(get_digest_value())