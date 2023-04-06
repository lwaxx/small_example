from django.http.response import FileResponse


def get(self, request):

    res_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'Templates')

    # asset_url为docx文件模板路径
    asset_url = os.path.join(res_dir, '说明.docx')
    file = open(asset_url, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = "application/msword"
    response['Content-Disposition'] = 'attachment;filename=说明.docx,'
    return response