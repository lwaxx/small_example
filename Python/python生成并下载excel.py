# pip install xlwt
import xlwt


def get(self, request):
    response = HttpResponse(content_type='application/vnd.ms-excel;charset=UTF-8')
    response['Content-Disposition'] = 'attachment;filename=海关信息报备表.xls,'
    wb = xlwt.Workbook(encoding='utf8')
    sheet = wb.add_sheet('sheet1')
    style_heading = xlwt.easyxf("""
                    font:
                        name SimSun,
                        bold on,
                        height 200;
                        align: wrap on,vert centre, horiz center;
                    align:
                        wrap off,
                        vert center,
                        horiz center;
                    borders:
                        left THIN,
                        right THIN,
                        top THIN,
                        bottom THIN;
                    """)
    style_desc = xlwt.easyxf("""
                    font:
                        name SimSun,
                        bold off,
                        colour_index red,
                        height 200;
                        align: wrap on,vert centre, horiz center;
                    align:
                        wrap on,
                        vert center,
                        horiz center;
                    borders:
                        left THIN,
                        right THIN,
                        top THIN,
                        bottom THIN;
                    """)
    sheet.write_merge(0, 0, 0, 14, '海关报备信息字段', style_heading)
    sheet.write(1, 0, '支付企业代码', style_heading)
    sheet.write(1, 1, '支付企业名称', style_heading)
    sheet.write(1, 2, '用户编号', style_heading)
    sheet.write(1, 3, '支付交易编号', style_heading)
    sheet.write(1, 4, '订单编号', style_heading)
    sheet.write(1, 5, '电商平台代码', style_heading)
    sheet.write(1, 6, '电商平台名称', style_heading)
    sheet.write(1, 7, '电商企业名称', style_heading)
    sheet.write(1, 8, '支付人证件类型', style_heading)
    sheet.write(1, 9, '支付人证件号码', style_heading)
    sheet.write(1, 10, '支付人姓名', style_heading)
    sheet.write(1, 11, '支付人手机号', style_heading)
    sheet.write(1, 12, '支付金额', style_heading)
    sheet.write(1, 13, '支付币制', style_heading)
    sheet.write(1, 14, '支付时间', style_heading)
    sheet.write(2, 0, '支付企业的海关注册登记编号', style_desc)
    sheet.write(2, 1, '报文传输的企业名称', style_desc)
    sheet.write(2, 2, '向中国电子口岸数据中心申请数据交换平台的用户编号', style_desc)
    sheet.write(2, 3, '支付企业唯一的支付流水号', style_desc)
    sheet.write(2, 4, '交易平台的订单编号，同一交易平台的订单编号应唯一', style_desc)
    sheet.write(2, 5, '电商平台的海关注册登记编 号；电商平台未在海关注册 登记，由电商企业发送订单 的，以中国电子口岸发布的 电商平台标识编号为准', style_desc)
    sheet.write(2, 6, '电商平台的海关注册登记名 称；电商平台未在海关注册 登记，由电商企业发送订单 的，以中国电子口岸发布的 电商平台名称为准', style_desc)
    sheet.write(2, 7, '', style_desc)
    sheet.write(2, 8, '', style_desc)
    sheet.write(2, 9, '', style_desc)
    sheet.write(2, 10, '', style_desc)
    sheet.write(2, 11, '', style_desc)
    sheet.write(2, 12, '', style_desc)
    sheet.write(2, 13, '限定为人民币', style_desc)
    sheet.write(2, 14, '支付时间', style_desc)
    sheet.col(0).width = 250 * 18
    sheet.col(1).width = 250 * 18
    sheet.col(2).width = 250 * 18
    sheet.col(3).width = 250 * 18
    sheet.col(4).width = 250 * 18
    sheet.col(5).width = 250 * 18
    sheet.col(6).width = 250 * 18
    sheet.col(7).width = 250 * 18
    sheet.col(8).width = 250 * 18
    sheet.col(9).width = 250 * 18
    sheet.col(10).width = 250 * 18
    sheet.col(11).width = 250 * 18
    sheet.col(12).width = 250 * 18
    sheet.col(13).width = 250 * 18
    sheet.col(14).width = 250 * 18

    output = BytesIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response