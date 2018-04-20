from django.db import models

# Create your models here.
from django.utils import timezone


# 文章标签类
class Tag(models.Model):
   t_name = models.CharField(max_length=255,verbose_name='标签名')
   t_createtime = models.DateTimeField(null=True,default=timezone.now, db_index=True,verbose_name='创建时间')

   def __str__(self):
      return self.t_name

   class Meta:
      verbose_name_plural = '标签'


# 文章类
class Art(models.Model):
   a_title = models.CharField(max_length=255,verbose_name='书名')
   a_info = models.CharField(max_length=300,verbose_name='简介')
   a_content = models.TextField(verbose_name='内容' )
   a_img = models.ImageField(null=True,blank=True, upload_to="uploads",verbose_name='封面')
   a_addtime = models.DateTimeField(default=timezone.now, db_index=True,verbose_name='创建时间',null=True,blank=True)
   a_updatetime = models.DateTimeField(default=timezone.now,verbose_name='更新时间',null=True,blank=True)
   a_tag = models.ForeignKey(Tag,blank=True,null=True,verbose_name='标签名')

   def __str__(self):
      return self.a_title

   class Meta:
      ordering = ['-a_addtime']
      verbose_name_plural = '文章'
