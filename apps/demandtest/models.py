from django.db import models
from datetime import datetime
from users.models import UserProfile
from boltons.fileutils import file
# Create your models here.
class ForeignDataTestCase(models.Model):
    TRAN_CODE = models.CharField(max_length=100, blank=True,verbose_name='交易码')
    REMARK1 = models.CharField(max_length=100, blank=True,default='',verbose_name='姓名')
    REMARK2 = models.CharField(max_length=100, blank=True,default='',verbose_name='身份证')
    REMARK3 = models.CharField(max_length=100, blank=True,default='9', verbose_name='备注1')
    REMARK4 = models.CharField(max_length=100, blank=True,default='9', verbose_name='备注2')
    BODYXML = models.TextField(verbose_name='返回的报文体')
    uploadTime = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    editor = models.ForeignKey(UserProfile, verbose_name="编辑者", blank=True, null=True)
    class Meta:
        verbose_name = '外部数据测试案例'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.TRAN_CODE+':外部数据测试案例-返回报文'