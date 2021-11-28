# pip install xhtml2pdf
import os

from django.http import HttpResponse
from xhtml2pdf import pisa


def get(self, request):

    res_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'Templates')

    # PDF格式下载
    response = HttpResponse(content_type='application/pdf;charset=UTF-8')
    response['Content-Disposition'] = 'attachment;filename=名字.pdf,'
    file_html = os.path.join(res_dir, 'fukuan.html')    # 模板文件的路径
    file_font = os.path.join(res_dir, 'simkai.ttf')  # 中文字体的路径
    with open(file_html, 'r') as f:
        html = f.read()
    
    context = {
        'order': self,
        'file_font': file_font,
        'text': '',
    }
    html = template.Template(html).render(template.Context(context, autoescape=False))
    file_io = BytesIO()
    pisa.CreatePDF(html, file_io)
    file_io.seek(0)
    response.write(file_io.getvalue())
    return response