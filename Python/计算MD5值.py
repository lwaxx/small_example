# -*- coding: utf-8 -*-

import base64
import binascii
import hashlib
from zlib import crc32

import sys
# 检查命令行参数
if len(sys.argv) < 2:
    print("请提供文件名作为参数！")
    sys.exit(1)
# 获取文件名参数
filename = sys.argv[1]


"""
计算字符串MD5值
"""
name = "7b2fe0ad65c6da4"
name_md5 = hashlib.md5()
name_md5.update(name.encode(encoding='utf-8'))
res_md5 = name_md5.hexdigest()
print(res_md5)     
print(res_md5.upper())  # 大写


"""
计算文件的MD5值
"""
md5 = hashlib.md5()

# 打开文件并逐块读取数据进行散列计算
with open(filename, 'rb') as file:
    while True:
        data = file.read(8192)  # 每次读取 8KB 数据
        if not data:
            break
        md5.update(data)
# 计算文件的 MD5 散列值
md5_hash = md5.hexdigest().upper()

print("MD5 Hash:", md5_hash)
