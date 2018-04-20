from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from art.models import Art, Tag

"""
文章展示列表

接口url

/art/art_list

method： GET



art应用的文章展示url和逻辑函数对应关系

"""


def ArtListHandler(request):
   key = request.GET.get("key", "")
   page = request.GET.get("page", 1)
   page = int(page)
   art_sets = Art.objects.filter(Q(a_title__contains=str(key))
                          | Q(a_content__contains=str(key))
                          | Q(a_info__contains=str(key))).distinct()
   total = art_sets.count()
   if total == 0:
      context = dict(
         pagenum=1,
         total=0,
         prev=1,
         next=1,
         pagerange=range(1, 2),
         data=[],
         url=request.path,
         key=key,
         page=page
      )
      return render(request, "statics/art_list.html", context=context)
   shownum = 10
   import math
   pagenum = int(math.ceil(total / shownum))
   if page < 1:
      return HttpResponseRedirect(request.path)
   if page > pagenum:
      return HttpResponse(request.path + "?page=%d" % pagenum)
   offset = (page - 1) * shownum
   data = art_sets[offset:shownum+offset]
   btnnum = 5
   if btnnum > pagenum:
      firstpage = 1
      lastpage = pagenum
   else:
      if page == 1:
         firstpage = 1
         lastpage = btnnum
      else:
         firstpage = page - 2
         lastpage = page + btnnum - 3
         if firstpage < 1:
            firstpage = 1
         if lastpage > pagenum:
            lastpage = pagenum
   prev = page - 1
   next = page + 1
   if prev < 1:
      prev = 1
   if next > pagenum:
      next = pagenum
   context = dict(
      pagenum=pagenum,
      total=total,
      prev=prev,
      next=next,
      pagerange=range(firstpage, lastpage + 1),
      data=data,
      url=request.path,
      key=key,
      page=page
   )

   return render(request, "statics/art_list.html", context=context)


def ArtEditGetHandler(request):
   tags = Tag.objects.all()
   id = request.GET.get("id", None)
   if id != None:
      id = int(id)
      art = Art.objects.get(id=id)
      context = {
         'tags': tags,
         'id': id,
         'art': art
      }
      return render(request, "statics/art_edit.html", context=context)
   else:
      context = {
         'tags': tags,
         'id': id,
      }
      return render(request, "statics/art_edit.html", context=context)


def ArtEditPostHandler(request):
   print('#######ArtEditPostHandler::POST')
   import json
   title = request.POST.get("title", "")
   info = request.POST.get("info", "")
   content = request.POST.get("content", "")
   img = request.POST.get("img", "")
   tag = request.POST.get("tag", 0)
   id = request.POST.get("id", "")
   res = dict(ok=1)
   if title == "":
      res["ok"] = 0
      res["title"] = "文章标题不能为空！"
   if info == "":
      res["ok"] = 0
      res["info"] = "文章简介不能为空！"
   if content == "":
      res["ok"] = 0
      res["content"] = "文章内容不能为空！"
   if img == "":
      res["ok"] = 0
      res["img"] = "文章封面不能为空！"
   if tag == "" and int(tag) != 0:
      res["ok"] = 0
      res["tag"] = "文章标签不能为空！"
   if res["ok"] == 1:
      if int(id) == 0:
         # sql = "insert into art(title,info,content,img,tag) values(:a,:b,:c,:d,:e)"
         art_inst = Art()
         art_inst.a_title = title
         art_inst.a_info = info
         art_inst.a_content = content
         art_inst.a_img = img
         art_inst.a_tag_id = int(tag)
         art_inst.save()
      else:
         # sql = "update art set title=:a,info=:b,content=:c,img=:d,tag=:e where id = :id"
         # self.db.execute(sql, dict(a=title, b=info, c=content, d=img, e=int(tag), id=int(id)))
         # self.db.commit()
         # self.db.close()
         arts = Art.objects.filter(a_title=title, a_info=info, a_content=content, a_img=img, a_tag_id=int(tag))
         arts.update(id=int(id))

   return HttpResponse(json.dumps(res))


def HistogramHandler(request):
   import json
   myjson = {
      'type': 'column',
      'colorByPoint': 'true',
      'data': [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
      'showInLegend': 'true'
   }
   data = json.dumps(myjson)
   return render(request, "statics/art_statics.html", locals())


def LinesHandler(request):
   return render(request, "statics/art_lines.html")
