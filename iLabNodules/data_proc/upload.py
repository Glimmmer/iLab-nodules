# -*- coding: utf-8 -*-
from django.http import HttpResponse


def upload(request):
    if not request.method == "POST":
        return HttpResponse("please use POST method!")
    else:
        my_file = request.FILES.get("upload", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not my_file:
            return HttpResponse("No files for upload!")
        else:
            # destination = open(os.path.join("/data/upload", my_file.name), 'wb+')    # 打开特定的文件进行二进制的写操作
            # for chunk in my_file.chunks():      # 分块写入文件
            #     destination.write(chunk)
            # destination.close()
            return HttpResponse("upload suc! the file name is " + str(my_file.name))
