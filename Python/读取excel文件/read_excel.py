import xlrd

data = xlrd.open_workbook(r'/home/user/Desktop/1.xlsx')
table = data.sheets()[0]

#创建一个空列表，存储Excel的数据
tables = []
 
 
#将excel表格内容导入到tables列表中
def import_excel(excel):
  for rown in range(excel.nrows):
   array = {'full_name':'','short_name':'','str_code':'','int_code':''}
   array['full_name'] = table.cell_value(rown,0)
   array['short_name'] = table.cell_value(rown,1)
   array['str_code'] = table.cell_value(rown,2)
   array['int_code'] = table.cell_value(rown,3)
   a = "INSERT INTO public.ams_country_code (full_name, short_name, str_code, int_code)  VALUES ('%s', '%s', '%s', '%s');"%(table.cell_value(rown,0).replace(" ", ""), table.cell_value(rown,1).replace(" ", ""), table.cell_value(rown,2), table.cell_value(rown,3))

   tables.append(a)


if __name__ == '__main__':
  #将excel表格的内容导入到列表中
    import_excel(table)
  #验证Excel文件存储到列表中的数据
    for i in tables:
        with open('/home/user/Desktop/1.sql', 'a+') as f:
            f.write(i + "\r\n")
        print(i)