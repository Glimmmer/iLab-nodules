# -*- coding: utf-8 -*-

from django.shortcuts import render


def index(request):
    context = {}
    nodules = {}
    nodules['id'] = 1
    nodules['z'] = 70
    nodules['y'] = 1
    nodules['x'] = 1

    data = []
    data.append(nodules)
    # data: nodules id and coordinates

    context['nodules'] = data
    return render(request, 'index.html', context)
