# -*- coding: utf-8 -*-

from django.http import JsonResponse
import load
from ..settings import BASE_DIR
import os


def load_img(request):
    res = {}
    mhd_file = os.path.join(BASE_DIR, "data/1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860.mhd")
    save_path = os.path.join(BASE_DIR, "index/static/image")
    cnt = load.load_img(mhd_file, save_path)
    res['max_cnt'] = cnt

    return JsonResponse(res)


def load_nodules(request):
    res = {}

    return JsonResponse(res)
