import hashlib
import os
import socket
import uuid
import binascii
import logging

from xml.dom.minidom import Document
from datetime import datetime

import rsa

logger = logging.getLogger()


# 在内存中创建一个空的文档
# doc = Document()
# # 创建一个根节点Managers对象
# root = doc.createElement('Managers')
# # 设置根节点的属性
# root.setAttribute('company', 'xx科技')
# root.setAttribute('address', '科技软件园')
# # 将根节点添加到文档对象中
# doc.appendChild(root)
#
# managerList = [{'name': 'joy', 'age': 27, 'sex': '女'},
#                {'name': 'tom', 'age': 30, 'sex': '男'},
#                {'name': 'ruby', 'age': 29, 'sex': '女'}
#                ]
#
# for i in managerList:
#     nodeManager = doc.createElement('Manager')
#     nodeName = doc.createElement('name')
#     # 给叶子节点name设置一个文本节点，用于显示文本内容
#     nodeName.appendChild(doc.createTextNode(str(i['name'])))
#
#     nodeAge = doc.createElement("age")
#     nodeAge.appendChild(doc.createTextNode(str(i["age"])))
#
#     nodeSex = doc.createElement("sex")
#     nodeSex.appendChild(doc.createTextNode(str(i["sex"])))
#
#     # 将各叶子节点添加到父节点Manager中，
#     # 最后将Manager添加到根节点Managers中
#     nodeManager.appendChild(nodeName)
#     nodeManager.appendChild(nodeAge)
#     nodeManager.appendChild(nodeSex)
#     root.appendChild(nodeManager)
# # 开始写xml文档
# fp = open('bookstore.xml', 'w')
# doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")

def get_digest_value(data):
    """生成摘要"""
    if not isinstance(data, bytes):
        data = str(data).encode('utf-8')
    sha = hashlib.sha1(data).hexdigest()
    return binascii.b2a_base64(binascii.unhexlify(sha)).decode().strip()


class Signature:
    """
    签名，获取证书
    """
    def __init__(self, DigestValue):
        SignatureValue = self.get_signature_value(DigestValue)  # 生成 SignatureValue

    def __str__(self):

        with open(r'./../../sign/509.pem', 'r') as f:
            X509Certificate = f.readlines()[1:-2]

        X509Certificate = ''.join(X509Certificate)
        return '\n' + X509Certificate

    def get_signature_value(self, signed_info):
        # 获取签名 rsa-sha1

        # # 加密平台
        # data = get_digest_value(signed_info)
        # return sign(data)

        # 加密机
        # return hsm(signed_info)

        # # rsa签名
        with open(r'./../../sign/rsa_private_key.pem', 'rb') as f:
            key = f.read()
        pri_key = rsa.PrivateKey.load_pkcs1(key)
        sha1 = rsa.sign(bytes(signed_info, encoding="utf8"), priv_key=pri_key, hash_method='SHA-1')
        return binascii.b2a_base64(sha1).decode().strip()



def createXml():
    """生成海关报备所需支付报文xml"""
    guid = str(uuid.uuid1()).upper()

    doc = Document()
    root = doc.createElement('ceb:CEB411Message')

    # 设置根节点属性
    root.setAttribute('guid', guid)
    root.setAttribute('version', '1.0')
    root.setAttribute('xmlns:ceb', "http://www.chinaport.gov.cn/ceb")
    root.setAttribute('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")

    # 将根节点添加到文档对象中
    doc.appendChild(root)
    appTime = datetime.now().strftime("%Y%m%d%H%M%S")

    _guid = str(uuid.uuid1()).upper()
    dict_pay = {
        "ceb:guid": _guid,
        "ceb:appType": "1",
        "ceb:appTime": appTime,
        "ceb:appStatus": 2,
        "ceb:payCode": "1101110323",
        "ceb:payName": "测试企业",
        "ceb:payTransactionId": "P0242250007",
        "ceb:orderNo": "order2016030811340007",
        "ceb:ebpCode": "1101110325",
        "ceb:ebpName": "测试企业",
        "ceb:payerIdType": 1,
        "ceb:payerIdNumber": "130625021345225322",
        "ceb:payerName": "支付人",
        "ceb:telephone": "13256254445",
        "ceb:amountPaid": "19050",
        "ceb:currency": "142",
        "ceb:payTime": "20160315153555",
        "ceb:note": "",
    }

    dict_transfer = {
        "ceb:copCode": "1101180326",
        "ceb:copName": "物流企业",
        "ceb:dxpMode": "DXP",
        "ceb:dxpId": "DXPLGS0000000001",
        "ceb:note": "",
    }

    keyName = "0001"

    nodePayment = doc.createElement('ceb:Payment')
    nodePaymentHead = doc.createElement('ceb:PaymentHead')

    node_guid = doc.createElement('ceb:guid')
    node_guid.appendChild(doc.createTextNode(str(dict_pay["ceb:guid"])))
    node_appType = doc.createElement('ceb:appType')
    node_appType.appendChild(doc.createTextNode(str(dict_pay["ceb:appType"])))
    node_appTime = doc.createElement('ceb:appTime')
    node_appTime.appendChild(doc.createTextNode(str(dict_pay["ceb:appTime"])))
    node_appStatus = doc.createElement('ceb:appStatus')
    node_appStatus.appendChild(doc.createTextNode(str(dict_pay["ceb:appStatus"])))
    node_payCode = doc.createElement('ceb:payCode')
    node_payCode.appendChild(doc.createTextNode(str(dict_pay["ceb:payCode"])))
    node_payName = doc.createElement('ceb:payName')
    node_payName.appendChild(doc.createTextNode(str(dict_pay["ceb:payName"])))
    node_payTransactionId = doc.createElement('ceb:payTransactionId')
    node_payTransactionId.appendChild(doc.createTextNode(str(dict_pay["ceb:payTransactionId"])))
    node_orderNo = doc.createElement('ceb:orderNo')
    node_orderNo.appendChild(doc.createTextNode(str(dict_pay["ceb:orderNo"])))
    node_ebpCode = doc.createElement('ceb:ebpCode')
    node_ebpCode.appendChild(doc.createTextNode(str(dict_pay["ceb:ebpCode"])))
    node_ebpName = doc.createElement('ceb:ebpName')
    node_ebpName.appendChild(doc.createTextNode(str(dict_pay["ceb:ebpName"])))
    node_payerIdType = doc.createElement('ceb:payerIdType')
    node_payerIdType.appendChild(doc.createTextNode(str(dict_pay["ceb:payerIdType"])))
    node_payerIdNumber = doc.createElement('ceb:payerIdNumber')
    node_payerIdNumber.appendChild(doc.createTextNode(str(dict_pay["ceb:payerIdNumber"])))
    node_payerName = doc.createElement('ceb:payerName')
    node_payerName.appendChild(doc.createTextNode(str(dict_pay["ceb:payerName"])))
    node_telephone = doc.createElement('ceb:telephone')
    node_telephone.appendChild(doc.createTextNode(str(dict_pay["ceb:telephone"])))
    node_amountPaid = doc.createElement('ceb:amountPaid')
    node_amountPaid.appendChild(doc.createTextNode(str(dict_pay["ceb:amountPaid"])))
    node_currency = doc.createElement('ceb:currency')
    node_currency.appendChild(doc.createTextNode(str(dict_pay["ceb:currency"])))
    node_payTime = doc.createElement('ceb:payTime')
    node_payTime.appendChild(doc.createTextNode(str(dict_pay["ceb:payTime"])))
    node_note = doc.createElement('ceb:note')
    node_note.appendChild(doc.createTextNode(str(dict_pay["ceb:note"])))

    # 将各叶子节点添加到父节点Manager中
    nodePayment.appendChild(nodePaymentHead)
    nodePaymentHead.appendChild(node_guid)
    nodePaymentHead.appendChild(node_appType)
    nodePaymentHead.appendChild(node_appTime)
    nodePaymentHead.appendChild(node_appStatus)
    nodePaymentHead.appendChild(node_payCode)
    nodePaymentHead.appendChild(node_payName)
    nodePaymentHead.appendChild(node_payTransactionId)
    nodePaymentHead.appendChild(node_orderNo)
    nodePaymentHead.appendChild(node_ebpCode)
    nodePaymentHead.appendChild(node_ebpName)
    nodePaymentHead.appendChild(node_payerIdType)
    nodePaymentHead.appendChild(node_payerIdNumber)
    nodePaymentHead.appendChild(node_payerName)
    nodePaymentHead.appendChild(node_telephone)
    nodePaymentHead.appendChild(node_amountPaid)
    nodePaymentHead.appendChild(node_currency)
    nodePaymentHead.appendChild(node_payTime)
    nodePaymentHead.appendChild(node_note)

    root.appendChild(nodePayment)

    nodeBaseTransfer = doc.createElement('ceb:BaseTransfer')
    node_copCode = doc.createElement('ceb:copCode')
    node_copCode.appendChild(doc.createTextNode(str(dict_transfer["ceb:copCode"])))
    node_copName = doc.createElement('ceb:copName')
    node_copName.appendChild(doc.createTextNode(str(dict_transfer["ceb:copName"])))
    node_dxpMode = doc.createElement('ceb:dxpMode')
    node_dxpMode.appendChild(doc.createTextNode(str(dict_transfer["ceb:dxpMode"])))
    node_dxpId = doc.createElement('ceb:dxpId')
    node_dxpId.appendChild(doc.createTextNode(str(dict_transfer["ceb:dxpId"])))
    node_note = doc.createElement('ceb:note')
    node_note.appendChild(doc.createTextNode(str(dict_transfer["ceb:note"])))
    nodeBaseTransfer.appendChild(node_copCode)
    nodeBaseTransfer.appendChild(node_copName)
    nodeBaseTransfer.appendChild(node_dxpMode)
    nodeBaseTransfer.appendChild(node_dxpId)
    nodeBaseTransfer.appendChild(node_note)
    root.appendChild(nodeBaseTransfer)

    result = doc.toxml(encoding='UTF-8').decode()
    DigestValue = get_digest_value(result)

    nodeSignature = doc.createElement('ds:Signature')
    nodeSignature.setAttribute('xmlns:ds', 'http://www.w3.org/2000/09/xmldsig#')

    nodeSignedInfo = doc.createElement('ds:SignedInfo')

    nodeCanonicalizationMethod = doc.createElement('ds:CanonicalizationMethod')
    nodeCanonicalizationMethod.setAttribute('Algorithm', 'http://www.w3.org/TR/2001/REC-xml-c14n-20010315')

    nodeSignatureMethod = doc.createElement('ds:SignatureMethod')
    nodeSignatureMethod.setAttribute('Algorithm', 'http://www.w3.org/2000/09/xmldsig#rsa-sha1')

    nodeReference = doc.createElement('ds:Reference')
    nodeReference.setAttribute('URI', '')
    nodeTransforms = doc.createElement('ds:Transforms')
    nodeTransform = doc.createElement('ds:Transform')
    nodeTransform.setAttribute('Algorithm', 'http://www.w3.org/2000/09/xmldsig#enveloped-signature')
    nodeDigestMethod = doc.createElement('ds:DigestMethod')
    nodeDigestMethod.setAttribute('Algorithm', 'http://www.w3.org/2000/09/xmldsig#sha1')
    nodeDigestValue = doc.createElement('ds:DigestValue')
    nodeDigestValue.appendChild(doc.createTextNode(str(DigestValue)))
    nodeTransforms.appendChild(nodeTransform)
    nodeReference.appendChild(nodeTransforms)
    nodeReference.appendChild(nodeDigestMethod)
    nodeReference.appendChild(nodeDigestValue)

    nodeSignedInfo.appendChild(nodeCanonicalizationMethod)
    nodeSignedInfo.appendChild(nodeSignatureMethod)
    nodeSignedInfo.appendChild(nodeReference)

    nodeSignatureValue = doc.createElement('ds:SignatureValue')
    nodeSignatureValue.appendChild(doc.createTextNode(str(Signature(DigestValue).get_signature_value(DigestValue))))

    nodeKeyInfo = doc.createElement('ds:KeyInfo')
    nodeKeyName = doc.createElement('ds:KeyName')
    nodeKeyName.appendChild(doc.createTextNode(str(keyName)))
    nodeX509Data = doc.createElement('ds:X509Data')
    nodeX509Certificate = doc.createElement('ds:X509Certificate')
    nodeX509Certificate.appendChild(doc.createTextNode(str(Signature(DigestValue).__str__())))
    nodeX509Data.appendChild(nodeX509Certificate)
    nodeKeyInfo.appendChild(nodeKeyName)
    nodeKeyInfo.appendChild(nodeX509Data)

    nodeSignature.appendChild(nodeSignedInfo)
    nodeSignature.appendChild(nodeSignatureValue)
    nodeSignature.appendChild(nodeKeyInfo)
    root.appendChild(nodeSignature)


    fp = open('bookstore.xml', 'w')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")

    return doc.toxml(encoding='utf-8').decode()


createXml()
