from django.contrib import admin
from art.models import Tag,Art
# Register your models here.


class ArtSite(admin.AdminSite):
    site_header = '美文'
    site_title = '美文后台管理系统'
    site_url = 'index'


my_site = ArtSite()


class ArtAdmin(admin.ModelAdmin):
    list_display = ['a_title','a_info','a_addtime','a_updatetime']
    search_fields = ('a_title',)
    raw_id_fields = ['a_tag']
    list_filter = ('a_title','a_addtime')


class ArtInline(admin.StackedInline):
    model = Art
    extra = 2


class TagAdmin(admin.ModelAdmin):
    list_display = ['t_name','t_createtime']
    inlines = [ArtInline,]


# admin.site.register(Tag,TagAdmin)
# admin.site.register(Art,ArtAdmin)
my_site.register(Tag,TagAdmin)
my_site.register(Art,ArtAdmin)