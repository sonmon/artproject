from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from art.models import Art,Tag
"""
应用主页面逻辑处理文件：art/views.py

首页卡片式页面展示：   

​      接口URL：  /art/index?page=1&t=1

​     方法：GET

​      输入参数说明：

​          page:   第几页

​          t:  标签类别，整数标识  eg: 0--全部   1--爱情小说  2—科幻小说

​      输出：

​            渲染首页卡片式页面      

逻辑Handler代码：
"""
import  logging
logger = logging.getLogger("django")


def IndexHandler(request):
    logger.info("IndexHandler request Handler begin")
    # 初始化页面
    url = request.path
    page = request.GET.get('page',1)
    t = request.GET.get('t',0)
    page = int(page)
    t = int(t)
    total = 0
    if t == 0:
        art_set = Art.objects.all()
        total = art_set.count()
    else:
        tag_id = "{0}".format(t)
        art_set = Art.objects.filter(a_tag_id=tag_id)
        total = art_set.count()
    tags = Tag.objects.all()
    context = dict(
        pagenum=1,
        total = 0,
        prev =1,
        next = 1,
        pagerange = range(1,2),
        data = [],
        url = url,
        tags = tags,
        page = page,
        t = t
    )
    # 设置分页判断
    if total > 0:
        shownum = 20
        import math
        pagenum = math.ceil(total / shownum)
        if page < 1:
            url = request.path + "?page=1&t=1"
            return HttpResponseRedirect(url)
        if page > pagenum:
            url = request.path + "?page=%s&t=%s" % (pagenum,t)
            return HttpResponseRedirect(url)
        offset = (page-1) * int(shownum)
        if t == 0:
            data = Art.objects.all()[offset:int(shownum)+offset]
        else:
            data = Art.objects.filter(a_tag_id=t)[offset:int(shownum)+offset]

        btnum = 5
        if btnum > pagenum:
            firstpage = 1
            lastpage = pagenum
        else:
            if page == 1:
                firstpage = 1
                lastpage = btnum

            else:
                firstpage = page - 2
                lastpage = page + btnum -2
                if firstpage < 1:
                    firstpage = 1
                if lastpage > pagenum:
                    lastpage = pagenum

        prev = page - 1
        next = page + 1
        if prev < 1 :
            prev = 1
        if next > pagenum:
            next = pagenum

        context = dict(
            pagenum=pagenum,
            total=total,
            prev=prev,
            next=next,
            pagerange=range(firstpage,lastpage+1),
            data=data,
            url=url,
            tags=tags,
            page=page,
            t=t,
        )
    logger.debug('query total:' + str(total))
    return render(request,"home/index.html",context=context)


