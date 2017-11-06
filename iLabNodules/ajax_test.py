# -*- coding: utf-8 -*-

from django.http import JsonResponse


def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'test1', 'zqxt': 'test2'}
    if request.method == 'GET':
        name_dict['cnt'] = request.GET['cnt']
        name_dict['path'] = 'image/ct_img_0_002.jpg'

    return JsonResponse(name_dict)
