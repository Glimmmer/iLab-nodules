# -*- coding: utf-8 -*-

from django.http import JsonResponse
import os
from settings import BASE_DIR


def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'test1', 'zqxt': 'test2'}
    if request.method == 'GET':
        cnt = request.GET['cnt']
        name_dict['cnt'] = cnt
        cnt = int(cnt)
        path = os.path.join(BASE_DIR, 'index/static/image/ct_' + str(cnt) + '.png')
        if os.path.isfile(path):
            name_dict['path'] = 'image/ct_' + str(cnt) + '.png'

    return JsonResponse(name_dict)
