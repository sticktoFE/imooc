import xadmin
from .models import DemandList
from import_export import resources

#为了导入导出
class DemandListResource(resources.ModelResource):
    class Meta:
        model = DemandList
        import_id_fields = ('serial',)
        #fields = ('TRAN_CODE', 'REMARK1','REMARK2', 'REMARK3','REMARK4','BODYXML',)
        # exclude = ()
@xadmin.sites.register(DemandList)
class DemandListAdmin(object):
    #list_display = ['TRAN_CODE', 'REMARK1', 'REMARK2', 'REMARK3', 'REMARK4','BODYXML','uploadTime']
    search_fields = ['type', 'name']
    list_filter = ['type', 'mainBPM']
    #编辑时设置只读
    readonly_fields = ['editor']
    #编辑时不显示
    #exclude = ['REMARK1', 'REMARK2', 'REMARK3', 'REMARK4','BODYXML']
    #增加导入导出功能
    import_export_args = {'import_resource_class': DemandListResource, 'export_resource_class': DemandListResource}