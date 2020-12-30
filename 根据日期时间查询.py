    def get(self, request):
        """
        账户余额查询
        """
        body = request.GET
        owner_id = body.get('owner_id')
        owner_role = body.get('owner_role')
        account_no = body.get('account_no')
        account_type = body.get('account_type')
        status = body.get('status')
        start_balance = body.get('start_balance')
        end_balance = body.get('end_balance')
        start_time = body.get('start_time')
        end_time = body.get('end_time')

        response = {
            'code': '15000',
            'msg': '无符合条件的查询结果',
            'data': '',
        }

        search_dict = dict()
        if owner_id:
            search_dict['owner_id'] = owner_id
        if owner_role:
            search_dict['owner_role'] = owner_role
        if account_no:
            search_dict['account_no'] = account_no
        if account_type:
            search_dict['account_type'] = account_type
        if status:
            search_dict['status'] = status
        if start_time and end_time:
            search_dict['create_time__gte'] = start_time
            search_dict['create_time__lte'] = end_time
        if start_time and not end_time:
            search_dict['create_time__gte'] = start_time
        if end_time and not start_time:
            search_dict['create_time__lte'] = end_time
        if start_balance and end_balance:
            search_dict['balance__gte'] = start_balance
            search_dict['balance__lte'] = end_balance
        if start_balance and not end_balance:
            search_dict['balance__gte'] = start_balance
        if end_balance and not start_balance:
            search_dict['balance__lte'] = end_balance

        try:
            data = Account.objects.filter(**search_dict)
        except Exception:
            response['msg'] = '参数有误'
        else:
            if data.exists():
                for j in data:
                    j.status = j.get_status_display()
                    j.owner_role = j.get_owner_role_display()
                    j.account_type = j.get_account_type_display()
                res = serializers.serialize('python', data, ensure_ascii=False)
                res_list = list()
                for i in res:
                    del i['pk']
                    del i['model']
                    res_list.append(i['fields'])
                response['code'] = '0000'
                response['msg'] = 'ok'
                response['data'] = res_list
                return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse(response)