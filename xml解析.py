from lxml import etree

def parse_xml():
    Xml = '<?xml version="1.0" encoding="utf-8" standalone="no"?><tdgService><respHeader><respCode>0000000</respCode><traceSerial>1419474703993</traceSerial><traceDate>20141225</traceDate><traceTime>103143</traceTime><retMsg>success!</retMsg></respHeader><Signature xmlns="http://www.w3.org/2000/09/xmldsig#"><SignedInfo><CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/><SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/><Reference URI=""><Transforms><Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/></Transforms><DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/><DigestValue>C/kPqGYvlNKm318KOHnjZZV2mlM=</DigestValue></Reference></SignedInfo><SignatureValue>PwIPSi5iDaAcDKODJ9XvcZbr+sCYdgsf/iaZG5ybWzv+s/xKJVulNbX6qTnLqI04KYb7Jon18WlS.OM815a7c9yj5bNpSrqp3iVQeaqDVy3Ml+EZmZIdgvVt1x95my1njyq7G5uNAowzbgvgTyAIl1eQS.0BmKvtWk4gyKo5JrBccmpi6SYZ2oGOqz8RWNuFwbMbj7TrwfSjqY6vGa63c8qlOYUzMkRKjDKPHs.NEwdhTgnLj1i6EWq2mW+svx5SIYRpmUH/FX4pIe+GmrU8RBVE8UYNfmvq82FL5+XlTAq0FHVQn8j.mZ85+q9LUtX+3I0hpenkBMgJ3YHjyHkd3ukj/Q==</SignatureValue></Signature></tdgService>'

    try:
        Xml = etree.fromstring(Xml.encode('utf-8'))
    except Exception:
        return '提交的不是xml数据，或者格式有误' 

    # 解析中行付款xml报文，生成付款信息
    respCode = Xml.xpath('/tdgService/respHeader/respCode/text()')[0]
    retMsg = Xml.xpath('/tdgService/respHeader/retMsg/text()')[0]
    # class Info:
    #     pass
    # info = Info()

    # li = {}
    # 解析xml文件, 获取孙级别的数据 tag: text
    # for Xml2 in Xml.getchildren():
    #     for Xml3 in Xml2.getchildren():
    #         # di = {}
    #         # setattr(info, Xml3.tag, Xml3.text)
    #         # di[Xml3.tag] = Xml3.text
    #         # li.update(di)
    #         if Xml3.tag == 'respCode' and Xml3.text == "0000000":
    #             return True
    #         else:
    #             return False
            

    if respCode == "0000000":
        return True, retMsg
    else:
        return False


print(parse_xml())