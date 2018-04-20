from django.conf.urls import url
from django.views.generic import RedirectView

from .views import *
from .index_handler import IndexHandler
from .search_handler import SearchHandler
from .detail import DetailHandler
from .statistic_handler import (ArtListHandler,
                                ArtEditGetHandler,
                                LinesHandler,
                                HistogramHandler,
                                ArtEditPostHandler)
urlpatterns = [
    url(r'^index/$', index),# 接口设计入口
    url(r'^art_post/',art_post),# post请求的接口设计


    url(r'^index_handler/$',IndexHandler),
    url(r'^search/$',SearchHandler),
    url(r'^detail/$',DetailHandler),

    url(r'^index_x/$',render_index),# 数据统计的接口设计入口
    url(r'^art_list/$',ArtListHandler),
    url(r'^art_edit/$',ArtEditGetHandler),
    url(r'^art_ed_post/$', ArtEditPostHandler),
    url(r'^art_lines/$',LinesHandler),
    url(r'^art_statics/$',HistogramHandler),
    url(r'^statics/', RedirectView.as_view(url='/art/art_statics')),

]