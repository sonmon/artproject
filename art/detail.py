from django.http import HttpResponseRedirect
from django.shortcuts import render

from art.models import Art

"""
详情页面功能：

​       接口URL：  /art/detail?id=7

​      方法：GET

​      输入参数说明：

​          id： 文章id，（点击某一个具体的文章，传入文章id)

​     输出：

​          渲染详情页面



1. 实现详情页逻辑层，逻辑art/detail_handler.py代码：

"""

def DetailHandler(request):
    print('DetailHandler#enter!')
    # id = self.get_argument("id", None)
    id = request.GET.get("id", None)
    print('DetailHandler#id:' + str(id))
    if id == None:
        return HttpResponseRedirect("/art/index_handler")
    else:
        art = Art.objects.get(id=int(id))
        context = {"art": art}
        return render(request, "home/detail.html", context=context)