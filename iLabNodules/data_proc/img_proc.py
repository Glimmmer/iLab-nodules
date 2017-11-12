# -*- coding: utf-8 -*-

from django.http import JsonResponse
import load
from ..settings import BASE_DIR
import os


def load_img(request):
    res = {}
    file_name = request.GET['src']
    mhd_file = os.path.join(BASE_DIR, "data/" + str(file_name))
    if os.path.isfile(mhd_file):
        save_path = os.path.join(BASE_DIR, "index/static/image")
        cnt = load.load_img(mhd_file, save_path)
        res['max_cnt'] = cnt
        print(request.GET['src'])

    return JsonResponse(res)


def load_nodules(request):
    file_name = request.GET['src']
    mhd_file = os.path.join(BASE_DIR, "data/" + str(file_name))
    res = {'nodules': [
        {'x': 1, 'y': 2, 'z': 10},
        {'x': 2, 'y': 4, 'z': 30},
        {'x': 1, 'y': 2, 'z': 76},
        {'x': 2, 'y': 4, 'z': 25},
        {'x': 1, 'y': 2, 'z': 98},
        {'x': 2, 'y': 4, 'z': 26},
        {'x': 1, 'y': 2, 'z': 13},
        {'x': 2, 'y': 4, 'z': 39},
        {'x': 1, 'y': 2, 'z': 11},
        {'x': 2, 'y': 4, 'z': 70},
        {'x': 1, 'y': 2, 'z': 80},
        {'x': 2, 'y': 4, 'z': 100}
    ]}
    return JsonResponse(res)
