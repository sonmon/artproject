import json

from django.shortcuts import render,HttpResponse

# Create your views here.
from art.models import Art


def index(request):
    # url = request.path
    # page = request.GET.get('page',1)
    # t = request.GET.get('t',1)
    # page = int(page)
    # t = int(t)
    # total = 0
    a = Art.objects.all()
    b = a.get(id=1)
    a_title = b.a_title
    a_info = b.a_info
    context = {
        'a_title':a_title,
        'a_info' :a_info,
    }


    context=json.dumps(context)

    return HttpResponse(context)

import logging
# post请求接口设计
def art_post(request):
    #logger = logging.getLogger("django")
    if request.method == 'POST':
        #print(request.POST.get('key1'))
        #logger.warning("this method is enter. ")
        recevie_data = {'key1':request.POST.get('key1'),'key2':request.POST.get('key2'),'status':200}
        context = json.dumps(recevie_data)

        return HttpResponse(context)
    elif request.method == 'GET':
        return HttpResponse('get ok')

    else:
        return HttpResponse('post error')









def render_index(request):
    return render(request, "statics/index.html")
