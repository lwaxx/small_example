from gmssl import sm4

import binascii


sm4_key = 'ky95TLsSRgFcAYoGW7vH1AK3boH06SOg9uoj49phN8PJMpb01l2YHL65vMgRfTszlAMoLcIB3v11DCm637Qz2ni4okIRrw+8WiAJkahsI47+rcU475+VnDtC875P6R5Dgd8zZg6O4w2XMPvbH9em+JGjdMFPG6GlQlBfTQPeszf9WRW6rzUV9p92+TVkzGztIP+1P7VnCKjMVr1nFECusxQbE2XQUPBLq8eK8Sf2zoSTPN94ei4j0fOAd75SEvnof6H95z7tHtcsj4kgCfvLYb75PH5Xtw6sdFye++O9oMnDlwET326rm31p3lQXAGiyAcVAAkM5gfQ6I00brRxSHg=='  # RSA私钥解密后, 不满16位则自动重复,取前16位

def SM4(input_data, encode=1):
    # SM4加密解密，默认为加密
    # gmssl==3.2.1

    if not isinstance(input_data, bytes):
        input_data = str(input_data).encode()

    key = (sm4_key * 16)[:16]
    if not isinstance(key, bytes):
        key = str(key).encode()

    crypt = sm4.CryptSM4()
    crypt_type = sm4.SM4_ENCRYPT if encode else sm4.SM4_DECRYPT
    crypt.set_key(key, crypt_type)

    try:
        return crypt.crypt_ecb(input_data)
    except Exception as e:
        print('Error: 国密SM4处理出错！！', e)
        return ''


if __name__ == "__main__":
    # 加密：encode=1    解密：encode=0

    data_jia_bytes = SM4('12345')
    data_jie_bytes = SM4(data_jia_bytes, encode=0)
    print(data_jia_bytes)     # bytes
    print(data_jie_bytes)     # bytes

    data_jia_str = SM4('12345').hex()
    data_jie_str = SM4(binascii.unhexlify(data_jia_str), encode=0).decode()
    print(data_jia_str)       # str
    print(data_jie_str)