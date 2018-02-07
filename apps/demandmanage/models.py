from django.db import models
from datetime import datetime
from users.models import UserProfile
from boltons.fileutils import file
# Create your models here.
class DemandList(models.Model):
    # 需求主题
    serial = models.CharField(max_length=100, null=True,blank=True, verbose_name='需求编号')
    type = models.CharField(max_length=100, null=True,blank=True, verbose_name='需求类型')
    name = models.CharField(max_length=100, default='无需求名称',null=True,blank=True, verbose_name='需求名称')
    description = models.TextField(null=True,blank=True, verbose_name='需求概述')
    mainBPM = models.CharField(max_length=100, null=True,blank=True, verbose_name='主办业务项目经理')
    coadjutantPM = models.CharField(max_length=100, null=True,blank=True, verbose_name='协办业务项目经理')
    applyDep = models.CharField(max_length=100, null=True,blank=True, verbose_name='申请部门')
    applyDate = models.DateField(max_length=100, null=True,blank=True, verbose_name='申请时间')
    expireFinishDate = models.DateField(max_length=100, null=True,blank=True, verbose_name='期望上线时间')
    evaluateFinishDate = models.DateField(max_length=100, null=True,blank=True, verbose_name='初估上线时间')
    emergency = models.CharField(max_length=100,null=True,blank=True, verbose_name='紧急程度')
    important = models.CharField(max_length=100, null=True,blank=True, verbose_name='重要程度')
    needFrameworkBlueprint = models.BooleanField(default=0,blank=True, verbose_name='是否编写架构方案')
    frameworkBlueprintResult = models.CharField(max_length=100, null=True,blank=True, verbose_name='架构方案评审结果')
    needSecurityBlueprint = models.BooleanField(default=0,blank=True, verbose_name='是否编写安全方案')
    securityBlueprintResult = models.CharField(max_length=100,null=True, blank=True, verbose_name='安全方案评审结果')
    demandStage = models.CharField(max_length=100, null=True,blank=True, verbose_name='需求阶段')
    demandStatus = models.CharField(max_length=100, null=True,blank=True, verbose_name='需求状态')
    demandProgressDescription = models.TextField(null=True,blank=True, verbose_name='进展说明')
    demandForDep = models.CharField(max_length=100, null=True,blank=True, verbose_name='需求归属分行')
    PM = models.CharField(max_length=100, null=True,blank=True, verbose_name='项目经理')
    PMForDep = models.CharField(max_length=100, null=True,blank=True, verbose_name='归属应用开发组')
    operationAssistant = models.CharField(max_length=100, null=True,blank=True, verbose_name='运维助理')
    mainDM = models.CharField(max_length=100, null=True,blank=True, verbose_name='主办需求经理')
    coadjutantDM = models.CharField(max_length=100, null=True,blank=True, verbose_name='协办需求经理')
    PMO = models.CharField(max_length=100, null=True,blank=True, verbose_name='PMO负责人')
    # 需求分析
    DemandAnalyzeOrProjectApprovePFD = models.DateField(max_length=100, null=True,blank=True, verbose_name='需求细化及评审/立项准备计划完成时间')
    DemandAnalyzeOrProjectApproveAFD = models.DateField(max_length=100, null=True,blank=True, verbose_name='需求细化及评审/立项准备实际完成时间')
    #排期
    scheduleName = models.CharField(max_length=100, null=True,blank=True, verbose_name='排期名称')
    scheduleDescription = models.TextField(null=True,blank=True, verbose_name='排期说明')
    shcedulePlanfinishDate = models.DateField(max_length=100, null=True,blank=True, verbose_name='排期计划上线时间')
    scheduleStage = models.CharField(max_length=100, null=True,blank=True, verbose_name='排期阶段')
    scheduleStatus = models.CharField(max_length=100, null=True,blank=True, verbose_name='排期状态')
    scheduleFinishRatio = models.CharField(max_length=6, null=True,blank=True, verbose_name='完成比例')
    scheduleProgressDescription = models.TextField(null=True,blank=True, verbose_name='进展说明')
    involvSystems = models.CharField(max_length=200, null=True,blank=True, verbose_name='相关系统')
    DemandAnalyzeOrProjectApprovePSD = models.DateField( null=True,blank=True, verbose_name='需求细化及评审/立项准备计划开始时间')
    DemandAnalyzeOrProjectApproveASD = models.DateField( null=True,blank=True, verbose_name='需求细化及评审/立项准备实际开始时间')
    DemandAnalyzeOrProjectApprovePED = models.DateField( null=True,blank=True, verbose_name='需求细化及评审/立项准备计划结束时间')
    DemandAnalyzeOrProjectApproveAED = models.DateField( null=True,blank=True, verbose_name='需求细化及评审/立项准备实际结束时间')
    DemandAnalyzeOrProjectApproveFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='需求细化及评审/立项准备完成百分比')
    DemandAnalyzeOrProjectApproveFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='需求细化及评审/立项准备完成情况')
    DemandOrFrameworkCompletePSD = models.DateField( null=True,blank=True, verbose_name='需求及架构完善计划开始时间')
    DemandOrFrameworkCompleteASD = models.DateField( null=True,blank=True, verbose_name='需求及架构完善实际开始时间')
    DemandOrFrameworkCompletePED = models.DateField( null=True,blank=True, verbose_name='需求及架构完善计划结束时间')
    DemandOrFrameworkCompleteAED = models.DateField( null=True,blank=True, verbose_name='需求及架构完善实际结束时间')
    DemandOrFrameworkCompleteFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='需求及架构完善完成百分比')
    DemandOrFrameworkCompleteFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='需求及架构完善完成情况')
    #软需
    SDemandCompletePSD = models.DateField( null=True,blank=True, verbose_name='软需编写及评审计划开始时间')
    SDemandCompleteASD = models.DateField( null=True,blank=True, verbose_name='软需编写及评审实际开始时间')
    SDemandCompletePED = models.DateField( null=True,blank=True, verbose_name='软需编写及评审计划结束时间')
    SDemandCompleteAED = models.DateField( null=True,blank=True, verbose_name='软需编写及评审实际结束时间')
    SDemandCompleteFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='软需编写及评审完成百分比')
    SDemandCompleteFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='软需编写及评审完成情况')

    outlineDesignPSD = models.DateField( null=True,blank=True, verbose_name='概要设计计划开始时间')
    outlineDesignASD = models.DateField( null=True,blank=True, verbose_name='概要设计实际开始时间')
    outlineDesignPED = models.DateField( null=True,blank=True, verbose_name='概要设计计划结束时间')
    outlineDesignAED = models.DateField( null=True,blank=True, verbose_name='概要设计实际结束时间')
    outlineDesignFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='概要设计完成百分比')
    outlineDesignFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='概要设计完成情况')

    detailDesignPSD = models.DateField( null=True,blank=True, verbose_name='详细设计计划开始时间')
    detailDesignASD = models.DateField( null=True,blank=True, verbose_name='详细设计实际开始时间')
    detailDesignPED = models.DateField( null=True,blank=True, verbose_name='详细设计计划结束时间')
    detailDesignAED = models.DateField( null=True,blank=True, verbose_name='详细设计实际结束时间')
    detailDesignFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='详细设计完成百分比')
    detailDesignFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='详细设计完成情况')

    unitTestPSD = models.DateField( null=True,blank=True, verbose_name='单元测试计划开始时间')
    unitTestASD = models.DateField( null=True,blank=True, verbose_name='单元测试实际开始时间')
    unitTestPED = models.DateField( null=True,blank=True, verbose_name='单元测试计划结束时间')
    unitTestAED = models.DateField( null=True,blank=True, verbose_name='单元测试实际结束时间')
    unitTestFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='单元测试完成百分比')
    unitTestFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='单元测试完成情况')

    integrationTestPSD = models.DateField( null=True,blank=True, verbose_name='集成测试计划开始时间')
    integrationTestASD = models.DateField( null=True,blank=True, verbose_name='集成测试实际开始时间')
    integrationTestPED = models.DateField( null=True,blank=True, verbose_name='集成测试计划结束时间')
    integrationTestAED = models.DateField( null=True,blank=True, verbose_name='集成测试实际结束时间')
    integrationTestFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='集成测试完成百分比')
    integrationTestFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='集成测试完成情况')

    SITTestPSD = models.DateField( null=True,blank=True, verbose_name='SIT测试善计划开始时间')
    SITTestASD = models.DateField( null=True,blank=True, verbose_name='SIT测试善实际开始时间')
    SITTestPED = models.DateField( null=True,blank=True, verbose_name='SIT测试善计划结束时间')
    SITTestAED = models.DateField( null=True,blank=True, verbose_name='SIT测试善实际结束时间')
    SITTestFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='SIT测试善完成百分比')
    SITTestFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='SIT测试善完成情况')

    UATTestPSD = models.DateField( null=True,blank=True, verbose_name='UAT测试计划开始时间')
    UATTestASD = models.DateField( null=True,blank=True, verbose_name='UAT测试实际开始时间')
    UATTestPED = models.DateField( null=True,blank=True, verbose_name='UAT测试计划结束时间')
    UATTestAED = models.DateField( null=True,blank=True, verbose_name='UAT测试实际结束时间')
    UATTestFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='UAT测试完成百分比')
    UATTestFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='UAT测试完成情况')

    regressionTestPSD = models.DateField( null=True,blank=True, verbose_name='回归测试计划开始时间')
    regressionTestASD = models.DateField( null=True,blank=True, verbose_name='回归测试实际开始时间')
    regressionTestPED = models.DateField( null=True,blank=True, verbose_name='回归测试计划结束时间')
    regressionTestAED = models.DateField( null=True,blank=True, verbose_name='回归测试实际结束时间')
    regressionTestFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='回归测试完成百分比')
    regressionTestFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='回归测试完成情况')

    nearOperationTestPSD = models.DateField( null=True,blank=True, verbose_name='准生产测试计划开始时间')
    nearOperationTestASD = models.DateField( null=True,blank=True, verbose_name='准生产测试实际开始时间')
    nearOperationTestPED = models.DateField( null=True,blank=True, verbose_name='准生产测试计划结束时间')
    nearOperationTestAED = models.DateField( null=True,blank=True, verbose_name='准生产测试实际结束时间')
    nearOperationTestFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='准生产测试完成百分比')
    nearOperationTestFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='准生产测试完成情况')

    goIntoOperationPSD = models.DateField( null=True,blank=True, verbose_name='投产实施计划开始时间')
    goIntoOperationASD = models.DateField( null=True,blank=True, verbose_name='投产实施实际开始时间')
    goIntoOperationPED = models.DateField( null=True,blank=True, verbose_name='投产实施计划结束时间')
    goIntoOperationAED = models.DateField( null=True,blank=True, verbose_name='投产实施实际结束时间')
    goIntoOperationFR = models.CharField(max_length=100, null=True,blank=True, verbose_name='投产实施完成百分比')
    goIntoOperationFD = models.CharField(max_length=100, null=True,blank=True, verbose_name='投产实施完成情况')
    editor = models.ForeignKey(UserProfile, verbose_name="编辑者", null=True,blank=True)
    class Meta:
        verbose_name = '需求清单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name