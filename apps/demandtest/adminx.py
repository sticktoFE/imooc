import xadmin
from .models import ForeignDataTestCase
from import_export import resources

#为了导入导出
class ForeignDataTestCaseResource(resources.ModelResource):
    class Meta:
        model = ForeignDataTestCase
        import_id_fields = ('TRAN_CODE',)
        fields = ('TRAN_CODE', 'REMARK1','REMARK2', 'REMARK3','REMARK4','BODYXML',)
        # exclude = ()
@xadmin.sites.register(ForeignDataTestCase)
class ForeignDataTestCaseAdmin(object):
    list_display = ['TRAN_CODE', 'REMARK1', 'REMARK2', 'REMARK3', 'REMARK4','BODYXML','uploadTime']
    search_fields = ['TRAN_CODE', 'REMARK1']
    list_filter = ['TRAN_CODE', 'REMARK1']
    #编辑设置
    readonly_fields = ['editor','uploadTime']
    #不显示
    exclude = ['REMARK1', 'REMARK2', 'REMARK3', 'REMARK4','BODYXML']
    import_export_args = {'import_resource_class': ForeignDataTestCaseResource, 'export_resource_class': ForeignDataTestCaseResource}
    """
    def save_models(self):
        obj = self.new_obj
        request=self.request
        obj.save()
        import_file(request,obj)
        
    #导入excel
    def post(self, request, *args, **kwargs):
        #xadmin 下templates/xadmin/excel/model_list.top_toolbar.import.html中
        #excel为导入文件名
        if 'excel' in request.FILES:
            importExcel(request.user,request.FILES['excel'])
        return super(ForeignDataTestCaseAdmin, self).post(request, *args, **kwargs)
    """