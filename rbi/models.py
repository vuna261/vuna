# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from pygments.lexer import default


class ApiComponentType(models.Model):
    apicomponenttypeid = models.IntegerField(db_column='APIComponentTypeID', primary_key=True)  # Field name made lowercase.
    apicomponenttypename = models.CharField(db_column='APIComponentTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gffsmall = models.FloatField(db_column='GFFSmall')  # Field name made lowercase.
    gffmedium = models.FloatField(db_column='GFFMedium')  # Field name made lowercase.
    gfflarge = models.FloatField(db_column='GFFLarge')  # Field name made lowercase.
    gffrupture = models.FloatField(db_column='GFFRupture')  # Field name made lowercase.
    gfftotal = models.FloatField(db_column='GFFTotal')  # Field name made lowercase.
    holecostsmall = models.FloatField(db_column='HoleCostSmall')  # Field name made lowercase.
    holecostmedium = models.FloatField(db_column='HoleCostMedium')  # Field name made lowercase.
    holecostlarge = models.FloatField(db_column='HoleCostLarge')  # Field name made lowercase.
    holecostrupture = models.FloatField(db_column='HoleCostRupture')  # Field name made lowercase.
    outagesmall = models.FloatField(db_column='OutageSmall')  # Field name made lowercase.
    outagemedium = models.FloatField(db_column='OutageMedium')  # Field name made lowercase.
    outagelarge = models.FloatField(db_column='OutageLarge')  # Field name made lowercase.
    outagerupture = models.FloatField(db_column='OutageRupture')  # Field name made lowercase.

    def __str__(self):
        return self.apicomponenttypename

    class Meta:
        managed = False
        db_table = 'api_component_type'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ComponentMaster(models.Model):
    componentid = models.AutoField(db_column='ComponentID', primary_key=True)  # Field name made lowercase.
    componentnumber = models.CharField(db_column='ComponentNumber', max_length=100)  # Field name made lowercase.
    equipmentid = models.ForeignKey('EquipmentMaster', on_delete=models.CASCADE, db_column='EquipmentID')  # Field name made lowercase.
    componenttypeid = models.ForeignKey('ComponentType', on_delete=models.CASCADE, db_column='ComponentTypeID')  # Field name made lowercase.
    componentname = models.CharField(db_column='ComponentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    componentdesc = models.CharField(db_column='ComponentDesc', max_length=250, blank=True, null=True)  # Field name made lowercase.
    isequipmentlinked = models.IntegerField(db_column='IsEquipmentLinked', default=0)  # Field name made lowercase.
    apicomponenttypeid = models.IntegerField(db_column='APIComponentTypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'component_master'


class ComponentType(models.Model):
    componenttypeid = models.IntegerField(db_column='ComponentTypeID', primary_key=True)  # Field name made lowercase.
    componenttypename = models.CharField(db_column='ComponentTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    componenttypecode = models.CharField(db_column='ComponentTypeCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.componenttypename
    class Meta:
        managed = False
        db_table = 'component_type'


class DesignCode(models.Model):
    designcodeid = models.AutoField(db_column='DesignCodeID', primary_key=True)  # Field name made lowercase.
    designcode = models.CharField(db_column='DesignCode', max_length=100)  # Field name made lowercase.
    designcodeapp = models.CharField(db_column='DesignCodeApp', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.designcode

    class Meta:
        managed = False
        db_table = 'design_code'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DmCategory(models.Model):
    dmcategoryid = models.IntegerField(db_column='DMCategoryID', primary_key=True)  # Field name made lowercase.
    dmcategoryname = models.CharField(db_column='DMCategoryName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dm_category'
        verbose_name = "Damage Category"


class DmItems(models.Model):
    dmitemid = models.IntegerField(db_column='DMItemID', primary_key=True)  # Field name made lowercase.
    dmdescription = models.CharField(db_column='DMDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dmseq = models.IntegerField(db_column='DMSeq', blank=True, null=True)  # Field name made lowercase.
    dmcategoryid = models.ForeignKey(DmCategory, on_delete=models.CASCADE, db_column='DMCategoryID', blank=True, null=True)  # Field name made lowercase.
    dmcode = models.CharField(db_column='DMCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hasdf = models.IntegerField(db_column='HasDF',default=0, blank=True, null=True)  # Field name made lowercase.
    failuremode = models.CharField(db_column='FailureMode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dm_items'
        verbose_name = "Damage Item"


class EquipmentMaster(models.Model):
    equipmentid = models.AutoField(db_column='EquipmentID', primary_key=True)  # Field name made lowercase.
    equipmentnumber = models.CharField(db_column='EquipmentNumber', max_length=100)  # Field name made lowercase.
    equipmenttypeid = models.ForeignKey('EquipmentType', on_delete=models.CASCADE, db_column='EquipmentTypeID')  # Field name made lowercase.
    equipmentname = models.CharField(db_column='EquipmentName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    commissiondate = models.DateTimeField(db_column='CommissionDate')  # Field name made lowercase.
    designcodeid = models.ForeignKey(DesignCode, on_delete=models.CASCADE, db_column='DesignCodeID')  # Field name made lowercase.
    siteid = models.ForeignKey('Sites', on_delete=models.CASCADE, db_column='SiteID')  # Field name made lowercase.
    facilityid = models.ForeignKey('Facility', on_delete=models.CASCADE, db_column='FacilityID')  # Field name made lowercase.
    manufacturerid = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, db_column='ManufacturerID')  # Field name made lowercase.
    pfdno = models.CharField(db_column='PFDNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    processdescription = models.CharField(db_column='ProcessDescription', max_length=250, blank=True, null=True)  # Field name made lowercase.
    equipmentdesc = models.CharField(db_column='EquipmentDesc', max_length=250, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.equipmentnumber

    class Meta:
        managed = False
        db_table = 'equipment_master'


class EquipmentType(models.Model):
    equipmenttypeid = models.IntegerField(db_column='EquipmentTypeID', primary_key=True)  # Field name made lowercase.
    equipmenttypecode = models.CharField(db_column='EquipmentTypeCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    equipmenttypename = models.CharField(db_column='EquipmentTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.equipmenttypename

    class Meta:
        managed = False
        db_table = 'equipment_type'


class Facility(models.Model):
    facilityid = models.AutoField(db_column='FacilityID', primary_key=True)  # Field name made lowercase.
    siteid = models.ForeignKey('Sites', on_delete=models.CASCADE, db_column='SiteID')  # Field name made lowercase.
    facilityname = models.CharField(db_column='FacilityName', max_length=100)  # Field name made lowercase.
    managementfactor = models.FloatField(db_column='ManagementFactor')  # Field name made lowercase.
    def __str__(self):
        return self.facilityname
    class Meta:
        managed = False
        db_table = 'facility'


class FacilityRiskTarget(models.Model):
    facilityid = models.ForeignKey(Facility,on_delete=models.CASCADE, db_column='FacilityID', primary_key=True)  # Field name made lowercase.
    risktarget_fc = models.FloatField(db_column='RiskTarget_FC', blank=True, null=True)  # Field name made lowercase.
    risktarget_ac = models.FloatField(db_column='RiskTarget_AC', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_risk_target'


class Manufacturer(models.Model):
    manufacturerid = models.AutoField(db_column='ManufacturerID', primary_key=True)  # Field name made lowercase.
    manufacturername = models.CharField(db_column='ManufacturerName', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return self.manufacturername

    class Meta:
        managed = False
        db_table = 'manufacturer'


class RwAssessment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(EquipmentMaster, on_delete=models.CASCADE, db_column='EquipmentID')  # Field name made lowercase.
    componentid = models.ForeignKey(ComponentMaster, on_delete=models.CASCADE, db_column='ComponentID')  # Field name made lowercase.
    assessmentdate = models.DateTimeField(db_column='AssessmentDate', blank=True, null=True)  # Field name made lowercase.
    riskanalysisperiod = models.IntegerField(db_column='RiskAnalysisPeriod')  # Field name made lowercase.
    isequipmentlinked = models.IntegerField(db_column='IsEquipmentLinked', default=0)  # Field name made lowercase.
    proposalname = models.CharField(db_column='ProposalName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.proposalname

    class Meta:
        managed = False
        db_table = 'rw_assessment'


class RwCaLevel1(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    release_phase = models.CharField(db_column='Release_Phase', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fact_di = models.FloatField(blank=True, null=True)
    fact_mit = models.FloatField(blank=True, null=True)
    fact_ait = models.FloatField(blank=True, null=True)
    ca_cmd = models.FloatField(db_column='CA_cmd', blank=True, null=True)  # Field name made lowercase.
    ca_inj_flame = models.FloatField(db_column='CA_inj_flame', blank=True, null=True)  # Field name made lowercase.
    ca_inj_toxic = models.FloatField(db_column='CA_inj_toxic', blank=True, null=True)  # Field name made lowercase.
    ca_inj_ntnf = models.FloatField(db_column='CA_inj_ntnf', blank=True, null=True)  # Field name made lowercase.
    fc_cmd = models.FloatField(db_column='FC_cmd', blank=True, null=True)  # Field name made lowercase.
    fc_affa = models.FloatField(db_column='FC_affa', blank=True, null=True)  # Field name made lowercase.
    fc_prod = models.FloatField(db_column='FC_prod', blank=True, null=True)  # Field name made lowercase.
    fc_inj = models.FloatField(db_column='FC_inj', blank=True, null=True)  # Field name made lowercase.
    fc_envi = models.FloatField(db_column='FC_envi', blank=True, null=True)  # Field name made lowercase.
    fc_total = models.FloatField(db_column='FC_total', blank=True, null=True)  # Field name made lowercase.
    fcof_category = models.CharField(db_column='FCOF_Category', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_ca_level1'


class RwCaTank(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    hydraulic_water = models.FloatField(db_column='Hydraulic_Water', blank=True, null=True)  # Field name made lowercase.
    hydraulic_fluid = models.FloatField(db_column='Hydraulic_Fluid', blank=True, null=True)  # Field name made lowercase.
    seepage_velocity = models.FloatField(db_column='Seepage_Velocity', blank=True, null=True)  # Field name made lowercase.
    flow_rate_d1 = models.FloatField(db_column='Flow_Rate_D1', blank=True, null=True)  # Field name made lowercase.
    flow_rate_d2 = models.FloatField(db_column='Flow_Rate_D2', blank=True, null=True)  # Field name made lowercase.
    flow_rate_d3 = models.FloatField(db_column='Flow_Rate_D3', blank=True, null=True)  # Field name made lowercase.
    flow_rate_d4 = models.FloatField(db_column='Flow_Rate_D4', blank=True, null=True)  # Field name made lowercase.
    leak_duration_d1 = models.FloatField(db_column='Leak_Duration_D1', blank=True, null=True)  # Field name made lowercase.
    leak_duration_d2 = models.FloatField(db_column='Leak_Duration_D2', blank=True, null=True)  # Field name made lowercase.
    leak_duration_d3 = models.FloatField(db_column='Leak_Duration_D3', blank=True, null=True)  # Field name made lowercase.
    leak_duration_d4 = models.FloatField(db_column='Leak_Duration_D4', blank=True, null=True)  # Field name made lowercase.
    release_volume_leak_d1 = models.FloatField(db_column='Release_Volume_Leak_D1', blank=True, null=True)  # Field name made lowercase.
    release_volume_leak_d2 = models.FloatField(db_column='Release_Volume_Leak_D2', blank=True, null=True)  # Field name made lowercase.
    release_volume_leak_d3 = models.FloatField(db_column='Release_Volume_Leak_D3', blank=True, null=True)  # Field name made lowercase.
    release_volume_leak_d4 = models.FloatField(db_column='Release_Volume_Leak_D4', blank=True, null=True)  # Field name made lowercase.
    release_volume_rupture = models.FloatField(db_column='Release_Volume_Rupture', blank=True, null=True)  # Field name made lowercase.
    liquid_height = models.FloatField(db_column='Liquid_Height', blank=True, null=True)  # Field name made lowercase.
    volume_fluid = models.FloatField(db_column='Volume_Fluid', blank=True, null=True)  # Field name made lowercase.
    time_leak_ground = models.FloatField(db_column='Time_Leak_Ground', blank=True, null=True)  # Field name made lowercase.
    volume_subsoil_leak_d1 = models.FloatField(db_column='Volume_SubSoil_Leak_D1', blank=True, null=True)  # Field name made lowercase.
    volume_subsoil_leak_d4 = models.FloatField(db_column='Volume_SubSoil_Leak_D4', blank=True, null=True)  # Field name made lowercase.
    volume_ground_water_leak_d1 = models.FloatField(db_column='Volume_Ground_Water_Leak_D1', blank=True, null=True)  # Field name made lowercase.
    volume_ground_water_leak_d4 = models.FloatField(db_column='Volume_Ground_Water_Leak_D4', blank=True, null=True)  # Field name made lowercase.
    barrel_dike_leak = models.FloatField(db_column='Barrel_Dike_Leak', blank=True, null=True)  # Field name made lowercase.
    barrel_dike_rupture = models.FloatField(db_column='Barrel_Dike_Rupture', blank=True, null=True)  # Field name made lowercase.
    barrel_onsite_leak = models.FloatField(db_column='Barrel_Onsite_Leak', blank=True, null=True)  # Field name made lowercase.
    barrel_onsite_rupture = models.FloatField(db_column='Barrel_Onsite_Rupture', blank=True, null=True)  # Field name made lowercase.
    barrel_offsite_leak = models.FloatField(db_column='Barrel_Offsite_Leak', blank=True, null=True)  # Field name made lowercase.
    barrel_offsite_rupture = models.FloatField(db_column='Barrel_Offsite_Rupture', blank=True, null=True)  # Field name made lowercase.
    barrel_water_leak = models.FloatField(db_column='Barrel_Water_Leak', blank=True, null=True)  # Field name made lowercase.
    barrel_water_rupture = models.FloatField(db_column='Barrel_Water_Rupture', blank=True, null=True)  # Field name made lowercase.
    fc_environ_leak = models.FloatField(db_column='FC_Environ_Leak', blank=True, null=True)  # Field name made lowercase.
    fc_environ_rupture = models.FloatField(db_column='FC_Environ_Rupture', blank=True, null=True)  # Field name made lowercase.
    fc_environ = models.FloatField(db_column='FC_Environ', blank=True, null=True)  # Field name made lowercase.
    material_factor = models.FloatField(db_column='Material_Factor', blank=True, null=True)  # Field name made lowercase.
    component_damage_cost = models.FloatField(db_column='Component_Damage_Cost', blank=True, null=True)  # Field name made lowercase.
    business_cost = models.FloatField(db_column='Business_Cost', blank=True, null=True)  # Field name made lowercase.
    consequence = models.FloatField(db_column='Consequence', blank=True, null=True)  # Field name made lowercase.
    consequencecategory = models.CharField(db_column='ConsequenceCategory', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_ca_tank'


class RwCoating(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    externalcoating = models.IntegerField(db_column='ExternalCoating',default=0, blank=True, null=True)  # Field name made lowercase.
    externalinsulation = models.IntegerField(db_column='ExternalInsulation',default=0, blank=True, null=True)  # Field name made lowercase.
    internalcladding = models.IntegerField(db_column='InternalCladding',default=0, blank=True, null=True)  # Field name made lowercase.
    internalcoating = models.IntegerField(db_column='InternalCoating',default=0, blank=True, null=True)  # Field name made lowercase.
    internallining = models.IntegerField(db_column='InternalLining',default=0, blank=True, null=True)  # Field name made lowercase.
    externalcoatingdate = models.DateTimeField(db_column='ExternalCoatingDate', blank=True, null=True)  # Field name made lowercase.
    externalcoatingquality = models.CharField(db_column='ExternalCoatingQuality', max_length=50, blank=True, null=True)  # Field name made lowercase.
    externalinsulationtype = models.CharField(db_column='ExternalInsulationType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    insulationcondition = models.CharField(db_column='InsulationCondition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    insulationcontainschloride = models.IntegerField(db_column='InsulationContainsChloride',default=0, blank=True, null=True)  # Field name made lowercase.
    internallinercondition = models.CharField(db_column='InternalLinerCondition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    internallinertype = models.CharField(db_column='InternalLinerType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    claddingcorrosionrate = models.FloatField(db_column='CladdingCorrosionRate', blank=True, null=True)  # Field name made lowercase.
    supportconfignotallowcoatingmaint = models.IntegerField(db_column='SupportConfigNotAllowCoatingMaint',default=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_coating'


class RwComponent(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    nominaldiameter = models.FloatField(db_column='NominalDiameter', blank=True, null=True)  # Field name made lowercase.
    nominalthickness = models.FloatField(db_column='NominalThickness', blank=True, null=True)  # Field name made lowercase.
    currentthickness = models.FloatField(db_column='CurrentThickness', blank=True, null=True)  # Field name made lowercase.
    minreqthickness = models.FloatField(db_column='MinReqThickness', blank=True, null=True)  # Field name made lowercase.
    currentcorrosionrate = models.FloatField(db_column='CurrentCorrosionRate', blank=True, null=True)  # Field name made lowercase.
    branchdiameter = models.CharField(db_column='BranchDiameter', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchjointtype = models.CharField(db_column='BranchJointType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    brinnelhardness = models.CharField(db_column='BrinnelHardness', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chemicalinjection = models.IntegerField(db_column='ChemicalInjection', default=0, blank=True, null=True)  # Field name made lowercase.
    highlyinjectioninsp = models.IntegerField(db_column='HighlyInjectionInsp', default=0, blank=True, null=True)  # Field name made lowercase.
    complexityprotrusion = models.CharField(db_column='ComplexityProtrusion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    correctiveaction = models.CharField(db_column='CorrectiveAction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crackspresent = models.IntegerField(db_column='CracksPresent', default=0, blank=True, null=True)  # Field name made lowercase.
    cyclicloadingwitin15_25m = models.CharField(db_column='CyclicLoadingWitin15_25m', max_length=50, blank=True, null=True)  # Field name made lowercase.
    damagefoundinspection = models.IntegerField(db_column='DamageFoundInspection',default=0, blank=True, null=True)  # Field name made lowercase.
    deltafatt = models.FloatField(db_column='DeltaFATT', blank=True, null=True)  # Field name made lowercase.
    numberpipefittings = models.CharField(db_column='NumberPipeFittings', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pipecondition = models.CharField(db_column='PipeCondition', max_length=50, blank=True, null=True)  # Field name made lowercase.
    previousfailures = models.CharField(db_column='PreviousFailures', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shakingamount = models.CharField(db_column='ShakingAmount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shakingdetected = models.IntegerField(db_column='ShakingDetected',default=0, blank=True, null=True)  # Field name made lowercase.
    shakingtime = models.CharField(db_column='ShakingTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trampelements = models.IntegerField(db_column='TrampElements',default=0, blank=True, null=True)  # Field name made lowercase.
    shellheight = models.FloatField(db_column='ShellHeight', blank=True, null=True)  # Field name made lowercase.
    releasepreventionbarrier = models.IntegerField(db_column='ReleasePreventionBarrier',default=0, blank=True, null=True)  # Field name made lowercase.
    concretefoundation = models.IntegerField(db_column='ConcreteFoundation',default=0, blank=True, null=True)  # Field name made lowercase.
    severityofvibration = models.CharField(db_column='SeverityOfVibration', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_component'


class RwEquipment(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    commissiondate = models.DateTimeField(db_column='CommissionDate')  # Field name made lowercase.
    adminupsetmanagement = models.IntegerField(db_column='AdminUpsetManagement', default=0)  # Field name made lowercase.
    containsdeadlegs = models.IntegerField(db_column='ContainsDeadlegs', default=0, blank=True, null=True)  # Field name made lowercase.
    cyclicoperation = models.IntegerField(db_column='CyclicOperation',default= 0, blank=True, null=True)  # Field name made lowercase.
    highlydeadleginsp = models.IntegerField(db_column='HighlyDeadlegInsp',default=0, blank=True, null=True)  # Field name made lowercase.
    downtimeprotectionused = models.IntegerField(db_column='DowntimeProtectionUsed',default=0, blank=True, null=True)  # Field name made lowercase.
    externalenvironment = models.CharField(db_column='ExternalEnvironment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    heattraced = models.IntegerField(db_column='HeatTraced',default=0, blank=True, null=True)  # Field name made lowercase.
    interfacesoilwater = models.IntegerField(db_column='InterfaceSoilWater',default=0, blank=True, null=True)  # Field name made lowercase.
    lineronlinemonitoring = models.IntegerField(db_column='LinerOnlineMonitoring',default=0, blank=True, null=True)  # Field name made lowercase.
    materialexposedtoclext = models.IntegerField(db_column='MaterialExposedToClExt',default=0, blank=True, null=True)  # Field name made lowercase.
    minreqtemperaturepressurisation = models.FloatField(db_column='MinReqTemperaturePressurisation', blank=True, null=True)  # Field name made lowercase.
    onlinemonitoring = models.CharField(db_column='OnlineMonitoring', max_length=100, blank=True, null=True)  # Field name made lowercase.
    presencesulphideso2 = models.IntegerField(db_column='PresenceSulphidesO2',default=0, blank=True, null=True)  # Field name made lowercase.
    presencesulphideso2shutdown = models.IntegerField(db_column='PresenceSulphidesO2Shutdown',default=0, blank=True, null=True)  # Field name made lowercase.
    pressurisationcontrolled = models.IntegerField(db_column='PressurisationControlled',default=0, blank=True, null=True)  # Field name made lowercase.
    pwht = models.IntegerField(db_column='PWHT',default=0, blank=True, null=True)  # Field name made lowercase.
    steamoutwaterflush = models.IntegerField(db_column='SteamOutWaterFlush',default=0, blank=True, null=True)  # Field name made lowercase.
    managementfactor = models.FloatField(db_column='ManagementFactor', blank=True, null=True)  # Field name made lowercase.
    thermalhistory = models.CharField(db_column='ThermalHistory', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yearlowestexptemp = models.IntegerField(db_column='YearLowestExpTemp',default=0, blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    typeofsoil = models.CharField(db_column='TypeOfSoil', max_length=50, blank=True, null=True)  # Field name made lowercase.
    environmentsensitivity = models.CharField(db_column='EnvironmentSensitivity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    distancetogroundwater = models.FloatField(db_column='DistanceToGroundWater', blank=True, null=True)  # Field name made lowercase.
    adjustmentsettle = models.CharField(db_column='AdjustmentSettle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    componentiswelded = models.IntegerField(db_column='ComponentIsWelded',default=0, blank=True, null=True)  # Field name made lowercase.
    tankismaintained = models.IntegerField(db_column='TankIsMaintained',default=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_equipment'


class RwExtcorTemperature(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    minus12tominus8 = models.FloatField(db_column='Minus12ToMinus8', blank=True, null=True)  # Field name made lowercase.
    minus8toplus6 = models.FloatField(db_column='Minus8ToPlus6', blank=True, null=True)  # Field name made lowercase.
    plus6toplus32 = models.FloatField(db_column='Plus6ToPlus32', blank=True, null=True)  # Field name made lowercase.
    plus32toplus71 = models.FloatField(db_column='Plus32ToPlus71', blank=True, null=True)  # Field name made lowercase.
    plus71toplus107 = models.FloatField(db_column='Plus71ToPlus107', blank=True, null=True)  # Field name made lowercase.
    plus107toplus121 = models.FloatField(db_column='Plus107ToPlus121', blank=True, null=True)  # Field name made lowercase.
    plus121toplus135 = models.FloatField(db_column='Plus121ToPlus135', blank=True, null=True)  # Field name made lowercase.
    plus135toplus162 = models.FloatField(db_column='Plus135ToPlus162', blank=True, null=True)  # Field name made lowercase.
    plus162toplus176 = models.FloatField(db_column='Plus162ToPlus176', blank=True, null=True)  # Field name made lowercase.
    morethanplus176 = models.FloatField(db_column='MoreThanPlus176', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_extcor_temperature'


class RwFullFcof(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    fcofvalue = models.FloatField(db_column='FCoFValue', blank=True, null=True)  # Field name made lowercase.
    fcofcategory = models.CharField(db_column='FCoFCategory', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ail = models.IntegerField(db_column='AIL', blank=True, null=True)  # Field name made lowercase.
    envcost = models.FloatField(blank=True, null=True)
    equipcost = models.FloatField(blank=True, null=True)
    prodcost = models.FloatField(blank=True, null=True)
    popdens = models.FloatField(blank=True, null=True)
    injcost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rw_full_fcof'


class RwFullPof(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    thinningap1 = models.FloatField(db_column='ThinningAP1', blank=True, null=True)  # Field name made lowercase.
    thinningap2 = models.FloatField(db_column='ThinningAP2', blank=True, null=True)  # Field name made lowercase.
    thinningap3 = models.FloatField(db_column='ThinningAP3', blank=True, null=True)  # Field name made lowercase.
    sccap1 = models.FloatField(db_column='SCCAP1', blank=True, null=True)  # Field name made lowercase.
    sccap2 = models.FloatField(db_column='SCCAP2', blank=True, null=True)  # Field name made lowercase.
    sccap3 = models.FloatField(db_column='SCCAP3', blank=True, null=True)  # Field name made lowercase.
    externalap1 = models.FloatField(db_column='ExternalAP1', blank=True, null=True)  # Field name made lowercase.
    externalap2 = models.FloatField(db_column='ExternalAP2', blank=True, null=True)  # Field name made lowercase.
    externalap3 = models.FloatField(db_column='ExternalAP3', blank=True, null=True)  # Field name made lowercase.
    brittleap1 = models.FloatField(db_column='BrittleAP1', blank=True, null=True)  # Field name made lowercase.
    brittleap2 = models.FloatField(db_column='BrittleAP2', blank=True, null=True)  # Field name made lowercase.
    brittleap3 = models.FloatField(db_column='BrittleAP3', blank=True, null=True)  # Field name made lowercase.
    htha_ap1 = models.FloatField(db_column='HTHA_AP1', blank=True, null=True)  # Field name made lowercase.
    htha_ap2 = models.FloatField(db_column='HTHA_AP2', blank=True, null=True)  # Field name made lowercase.
    htha_ap3 = models.FloatField(db_column='HTHA_AP3', blank=True, null=True)  # Field name made lowercase.
    fatigueap1 = models.FloatField(db_column='FatigueAP1', blank=True, null=True)  # Field name made lowercase.
    fatigueap2 = models.FloatField(db_column='FatigueAP2', blank=True, null=True)  # Field name made lowercase.
    fatigueap3 = models.FloatField(db_column='FatigueAP3', blank=True, null=True)  # Field name made lowercase.
    fms = models.FloatField(db_column='FMS', blank=True, null=True)  # Field name made lowercase.
    thinningtype = models.CharField(db_column='ThinningType', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gfftotal = models.FloatField(db_column='GFFTotal', blank=True, null=True)  # Field name made lowercase.
    thinninglocalap1 = models.FloatField(db_column='ThinningLocalAP1', blank=True, null=True)  # Field name made lowercase.
    thinninglocalap2 = models.FloatField(db_column='ThinningLocalAP2', blank=True, null=True)  # Field name made lowercase.
    thinninglocalap3 = models.FloatField(db_column='ThinningLocalAP3', blank=True, null=True)  # Field name made lowercase.
    thinninggeneralap1 = models.FloatField(db_column='ThinningGeneralAP1', blank=True, null=True)  # Field name made lowercase.
    thinninggeneralap2 = models.FloatField(db_column='ThinningGeneralAP2', blank=True, null=True)  # Field name made lowercase.
    thinninggeneralap3 = models.FloatField(db_column='ThinningGeneralAP3', blank=True, null=True)  # Field name made lowercase.
    totaldfap1 = models.FloatField(db_column='TotalDFAP1', blank=True, null=True)  # Field name made lowercase.
    totaldfap2 = models.FloatField(db_column='TotalDFAP2', blank=True, null=True)  # Field name made lowercase.
    totaldfap3 = models.FloatField(db_column='TotalDFAP3', blank=True, null=True)  # Field name made lowercase.
    pofap1 = models.FloatField(db_column='PoFAP1', blank=True, null=True)  # Field name made lowercase.
    pofap2 = models.FloatField(db_column='PoFAP2', blank=True, null=True)  # Field name made lowercase.
    pofap3 = models.FloatField(db_column='PoFAP3', blank=True, null=True)  # Field name made lowercase.
    pofap1category = models.CharField(db_column='PoFAP1Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pofap2category = models.CharField(db_column='PoFAP2Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pofap3category = models.CharField(db_column='PoFAP3Category', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_full_pof'


class RwInputCaLevel1(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    api_fluid = models.CharField(db_column='API_FLUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    system = models.CharField(db_column='SYSTEM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    release_duration = models.CharField(db_column='Release_Duration', max_length=50, blank=True, null=True)  # Field name made lowercase.
    detection_type = models.CharField(db_column='Detection_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isulation_type = models.CharField(db_column='Isulation_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mitigation_system = models.CharField(db_column='Mitigation_System', max_length=150, blank=True, null=True)  # Field name made lowercase.
    equipment_cost = models.FloatField(db_column='Equipment_Cost', blank=True, null=True)  # Field name made lowercase.
    injure_cost = models.FloatField(db_column='Injure_Cost', blank=True, null=True)  # Field name made lowercase.
    evironment_cost = models.FloatField(db_column='Evironment_Cost', blank=True, null=True)  # Field name made lowercase.
    toxic_percent = models.FloatField(db_column='Toxic_Percent', blank=True, null=True)  # Field name made lowercase.
    personal_density = models.FloatField(db_column='Personal_Density', blank=True, null=True)  # Field name made lowercase.
    material_cost = models.FloatField(db_column='Material_Cost', blank=True, null=True)  # Field name made lowercase.
    production_cost = models.FloatField(db_column='Production_Cost', blank=True, null=True)  # Field name made lowercase.
    mass_inventory = models.FloatField(db_column='Mass_Inventory', blank=True, null=True)  # Field name made lowercase.
    mass_component = models.FloatField(db_column='Mass_Component', blank=True, null=True)  # Field name made lowercase.
    stored_pressure = models.FloatField(db_column='Stored_Pressure', blank=True, null=True)  # Field name made lowercase.
    stored_temp = models.FloatField(db_column='Stored_Temp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_input_ca_level1'


class RwInputCaTank(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    fluid_height = models.FloatField(db_column='FLUID_HEIGHT', blank=True, null=True)  # Field name made lowercase.
    shell_course_height = models.FloatField(db_column='SHELL_COURSE_HEIGHT', blank=True, null=True)  # Field name made lowercase.
    tank_diametter = models.FloatField(db_column='TANK_DIAMETTER', blank=True, null=True)  # Field name made lowercase.
    prevention_barrier = models.IntegerField(db_column='Prevention_Barrier', default=0, blank=True, null=True)  # Field name made lowercase.
    environ_sensitivity = models.CharField(db_column='Environ_Sensitivity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_lvdike = models.FloatField(db_column='P_lvdike', blank=True, null=True)  # Field name made lowercase.
    p_onsite = models.FloatField(db_column='P_onsite', blank=True, null=True)  # Field name made lowercase.
    p_offsite = models.FloatField(db_column='P_offsite', blank=True, null=True)  # Field name made lowercase.
    soil_type = models.CharField(db_column='Soil_Type', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tank_fluid = models.CharField(db_column='TANK_FLUID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    api_fluid = models.CharField(db_column='API_FLUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sw = models.FloatField(db_column='SW', blank=True, null=True)  # Field name made lowercase.
    productioncost = models.FloatField(db_column='ProductionCost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_input_ca_tank'


class RwInspectionHistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    inspectionplanname = models.CharField(db_column='InspectionPlanName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inspectioncoveragename = models.CharField(db_column='InspectionCoverageName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    equipmentnumber = models.CharField(db_column='EquipmentNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    componentnumber = models.CharField(db_column='ComponentNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dm = models.CharField(db_column='DM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    inspectiontype = models.CharField(db_column='InspectionType', max_length=250, blank=True, null=True)  # Field name made lowercase.
    inspectiondate = models.DateTimeField(db_column='InspectionDate', blank=True, null=True)  # Field name made lowercase.
    inspectioneffective = models.CharField(db_column='InspectionEffective', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_inspection_history'


class RwMaterial(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    materialname = models.CharField(db_column='MaterialName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    designpressure = models.FloatField(db_column='DesignPressure', blank=True, null=True)  # Field name made lowercase.
    designtemperature = models.FloatField(db_column='DesignTemperature', blank=True, null=True)  # Field name made lowercase.
    mindesigntemperature = models.FloatField(db_column='MinDesignTemperature', blank=True, null=True)  # Field name made lowercase.
    brittlefracturethickness = models.FloatField(db_column='BrittleFractureThickness', blank=True, null=True)  # Field name made lowercase.
    corrosionallowance = models.FloatField(db_column='CorrosionAllowance', blank=True, null=True)  # Field name made lowercase.
    sigmaphase = models.FloatField(db_column='SigmaPhase', blank=True, null=True)  # Field name made lowercase.
    sulfurcontent = models.CharField(db_column='SulfurContent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    heattreatment = models.CharField(db_column='HeatTreatment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    referencetemperature = models.FloatField(db_column='ReferenceTemperature', blank=True, null=True)  # Field name made lowercase.
    ptamaterialcode = models.CharField(db_column='PTAMaterialCode', max_length=70, blank=True, null=True)  # Field name made lowercase.
    hthamaterialcode = models.CharField(db_column='HTHAMaterialCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispta = models.IntegerField(db_column='IsPTA',default=0, blank=True, null=True)  # Field name made lowercase.
    ishtha = models.IntegerField(db_column='IsHTHA',default=0, blank=True, null=True)  # Field name made lowercase.
    austenitic = models.IntegerField(db_column='Austenitic',default=0, blank=True, null=True)  # Field name made lowercase.
    temper = models.IntegerField(db_column='Temper',default=0, blank=True, null=True)  # Field name made lowercase.
    carbonlowalloy = models.IntegerField(db_column='CarbonLowAlloy',default=0, blank=True, null=True)  # Field name made lowercase.
    nickelbased = models.IntegerField(db_column='NickelBased',default=0, blank=True, null=True)  # Field name made lowercase.
    chromemoreequal12 = models.IntegerField(db_column='ChromeMoreEqual12',default=0, blank=True, null=True)  # Field name made lowercase.
    allowablestress = models.FloatField(db_column='AllowableStress', blank=True, null=True)  # Field name made lowercase.
    costfactor = models.FloatField(db_column='CostFactor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_material'


class RwStream(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)  # Field name made lowercase.
    aminesolution = models.CharField(db_column='AmineSolution', max_length=50, blank=True, null=True)  # Field name made lowercase.
    aqueousoperation = models.IntegerField(db_column='AqueousOperation',default=0, blank=True, null=True)  # Field name made lowercase.
    aqueousshutdown = models.IntegerField(db_column='AqueousShutdown',default=0, blank=True, null=True)  # Field name made lowercase.
    toxicconstituent = models.IntegerField(db_column='ToxicConstituent',default=0, blank=True, null=True)  # Field name made lowercase.
    caustic = models.IntegerField(db_column='Caustic',default=0, blank=True, null=True)  # Field name made lowercase.
    chloride = models.FloatField(db_column='Chloride', blank=True, null=True)  # Field name made lowercase.
    co3concentration = models.FloatField(db_column='CO3Concentration', blank=True, null=True)  # Field name made lowercase.
    cyanide = models.IntegerField(db_column='Cyanide',default=0, blank=True, null=True)  # Field name made lowercase.
    exposedtogasamine = models.IntegerField(db_column='ExposedToGasAmine',default=0, blank=True, null=True)  # Field name made lowercase.
    exposedtosulphur = models.IntegerField(db_column='ExposedToSulphur',default=0, blank=True, null=True)  # Field name made lowercase.
    exposuretoamine = models.CharField(db_column='ExposureToAmine', max_length=50, blank=True, null=True)  # Field name made lowercase.
    h2s = models.IntegerField(db_column='H2S',default=0, blank=True, null=True)  # Field name made lowercase.
    h2sinwater = models.FloatField(db_column='H2SInWater', blank=True, null=True)  # Field name made lowercase.
    hydrogen = models.IntegerField(db_column='Hydrogen',default=0, blank=True, null=True)  # Field name made lowercase.
    h2spartialpressure = models.FloatField(db_column='H2SPartialPressure', blank=True, null=True)  # Field name made lowercase.
    hydrofluoric = models.IntegerField(db_column='Hydrofluoric',default=0, blank=True, null=True)  # Field name made lowercase.
    materialexposedtoclint = models.IntegerField(db_column='MaterialExposedToClInt',default=0, blank=True, null=True)  # Field name made lowercase.
    maxoperatingpressure = models.FloatField(db_column='MaxOperatingPressure', blank=True, null=True)  # Field name made lowercase.
    maxoperatingtemperature = models.FloatField(db_column='MaxOperatingTemperature', blank=True, null=True)  # Field name made lowercase.
    minoperatingpressure = models.FloatField(db_column='MinOperatingPressure', blank=True, null=True)  # Field name made lowercase.
    minoperatingtemperature = models.FloatField(db_column='MinOperatingTemperature', blank=True, null=True)  # Field name made lowercase.
    criticalexposuretemperature = models.FloatField(db_column='CriticalExposureTemperature', blank=True, null=True)  # Field name made lowercase.
    naohconcentration = models.FloatField(db_column='NaOHConcentration', blank=True, null=True)  # Field name made lowercase.
    releasefluidpercenttoxic = models.FloatField(db_column='ReleaseFluidPercentToxic', blank=True, null=True)  # Field name made lowercase.
    waterph = models.FloatField(db_column='WaterpH', blank=True, null=True)  # Field name made lowercase.
    tankfluidname = models.CharField(db_column='TankFluidName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fluidheight = models.FloatField(db_column='FluidHeight', blank=True, null=True)  # Field name made lowercase.
    fluidleavedikepercent = models.FloatField(db_column='FluidLeaveDikePercent', blank=True, null=True)  # Field name made lowercase.
    fluidleavedikeremainonsitepercent = models.FloatField(db_column='FluidLeaveDikeRemainOnSitePercent', blank=True, null=True)  # Field name made lowercase.
    fluidgooffsitepercent = models.FloatField(db_column='FluidGoOffSitePercent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rw_stream'


class Sites(models.Model):
    siteid = models.AutoField(db_column='SiteID', primary_key=True)  # Field name made lowercase.
    sitename = models.CharField(db_column='SiteName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.sitename
    # def get_absolute_url(self):
    #     return reversed('site-detail', args=[str(self.sitename)])

    class Meta:
        managed = False
        db_table = 'sites'


class Tbl204DmHtha(models.Model):
    susceptibility = models.TextField(db_column='Susceptibility', blank=True, null=True)  # Field name made lowercase.
    no_inspection = models.IntegerField(db_column='No Inspection', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_1d = models.IntegerField(db_column='1D', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1c = models.IntegerField(db_column='1C', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1b = models.IntegerField(db_column='1B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2d = models.IntegerField(db_column='2D', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2c = models.IntegerField(db_column='2C', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'tbl_204_dm_htha'
        verbose_name = "Table 20.4 – Damage Factor - HTHA"


class Tbl213DmImpactExemption(models.Model):
    componentthickness = models.FloatField(db_column='ComponentThickness', blank=True, null=True)  # Field name made lowercase.
    curvea = models.FloatField(db_column='CurveA', blank=True, null=True)  # Field name made lowercase.
    curveb = models.FloatField(db_column='CurveB', blank=True, null=True)  # Field name made lowercase.
    curvec = models.FloatField(db_column='CurveC', blank=True, null=True)  # Field name made lowercase.
    curved = models.FloatField(db_column='CurveD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_213_dm_impact_exemption'
        verbose_name = "Table 21.3 – Impact Test Exemption Temperature"


class Tbl214DmNotPwht(models.Model):
    tmin_tref = models.IntegerField(db_column='Tmin-Tref', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_6_4 = models.FloatField(db_column='6.4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_7 = models.FloatField(db_column='12.7', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_25_4 = models.FloatField(db_column='25.4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_38_1 = models.FloatField(db_column='38.1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_50_8 = models.FloatField(db_column='50.8', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_63_5 = models.FloatField(db_column='63.5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_76_2 = models.FloatField(db_column='76.2', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_88_9 = models.FloatField(db_column='88.9', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_101_6 = models.FloatField(db_column='101.6', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'tbl_214_dm_not_pwht'
        verbose_name = "Table 21.4M – Damage Factor, Component Not Subject to PWHT – Brittle Fracture"


class Tbl215DmPwht(models.Model):
    tmin_tref = models.IntegerField(db_column='Tmin-Tref', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_6_4 = models.FloatField(db_column='6.4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_12_7 = models.FloatField(db_column='12.7', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_25_4 = models.FloatField(db_column='25.4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_38_1 = models.FloatField(db_column='38.1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_50_8 = models.FloatField(db_column='50.8', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_63_5 = models.FloatField(db_column='63.5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_76_2 = models.FloatField(db_column='76.2', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_88_9 = models.FloatField(db_column='88.9', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_101_6 = models.FloatField(db_column='101.6', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'tbl_215_dm_pwht'
        verbose_name = "Table 21.5M – Damage Factor, Component Subject to PWHT – Brittle Fracture"


class Tbl3B21SiConversion(models.Model):
    conversionfactory = models.IntegerField(db_column='conversionFactory', blank=True, null=True)  # Field name made lowercase.
    siunits = models.FloatField(db_column='SIUnits', blank=True, null=True)  # Field name made lowercase.
    usunits = models.FloatField(db_column='USUnits', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_3b21_si_conversion'
        verbose_name = "Table 3.B.2.1 – SI and US Customary Conversion Factor"


class Tbl511DfbThin(models.Model):
    art = models.FloatField(blank=True, null=True)
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    insp = models.IntegerField(blank=True, null=True)
    d = models.IntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    c = models.IntegerField(db_column='C', blank=True, null=True)  # Field name made lowercase.
    b = models.IntegerField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_511_dfb_thin'
        verbose_name = "Table 5.11 – Thinning Damage Factor"


class Tbl512DfbThinTankBottom(models.Model):
    art = models.FloatField(blank=True, null=True)
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    insp = models.IntegerField(blank=True, null=True)
    d = models.IntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    c = models.IntegerField(db_column='C', blank=True, null=True)  # Field name made lowercase.
    b = models.IntegerField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    a = models.IntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_512_dfb_thin_tank_bottom'
        verbose_name = "Table 5.12 – Thinning Damage Factors for Tank Bottom"


class Tbl52CaPropertiesLevel1(models.Model):
    fluid = models.TextField(db_column='Fluid', blank=True, null=True)  # Field name made lowercase.
    mw = models.FloatField(db_column='MW', blank=True, null=True)  # Field name made lowercase.
    density = models.FloatField(db_column='Density', blank=True, null=True)  # Field name made lowercase.
    nbp = models.FloatField(db_column='NBP', blank=True, null=True)  # Field name made lowercase.
    ambient = models.TextField(db_column='Ambient', blank=True, null=True)  # Field name made lowercase.
    ideal = models.IntegerField(blank=True, null=True)
    a = models.FloatField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    b = models.FloatField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    c = models.FloatField(db_column='C', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    e = models.FloatField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    auto = models.FloatField(db_column='Auto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_52_ca_properties_level_1'
        verbose_name = "Table 5.2 – Properties of the Representative Fluids Used in Level 1 Analysi"


class Tbl58CaComponentDm(models.Model):
    fluid = models.TextField(db_column='Fluid', blank=True, null=True)  # Field name made lowercase.
    cainl_gas_a = models.FloatField(db_column='CAINL_gas_a', blank=True, null=True)  # Field name made lowercase.
    cainl_gas_b = models.FloatField(db_column='CAINL_gas_b', blank=True, null=True)  # Field name made lowercase.
    cainl_liquid_a = models.FloatField(db_column='CAINL_liquid_a', blank=True, null=True)  # Field name made lowercase.
    cainl_liquid_b = models.FloatField(db_column='CAINL_liquid_b', blank=True, null=True)  # Field name made lowercase.
    cail_gas_a = models.FloatField(db_column='CAIL_gas_a', blank=True, null=True)  # Field name made lowercase.
    cail_gas_b = models.FloatField(db_column='CAIL_gas_b', blank=True, null=True)  # Field name made lowercase.
    cail_liquid_a = models.FloatField(db_column='CAIL_liquid_a', blank=True, null=True)  # Field name made lowercase.
    cail_liquid_b = models.FloatField(db_column='CAIL_liquid_b', blank=True, null=True)  # Field name made lowercase.
    iainl_gas_a = models.FloatField(db_column='IAINL_gas_a', blank=True, null=True)  # Field name made lowercase.
    iainl_gas_b = models.FloatField(db_column='IAINL_gas_b', blank=True, null=True)  # Field name made lowercase.
    iainl_liquid_a = models.FloatField(db_column='IAINL_liquid_a', blank=True, null=True)  # Field name made lowercase.
    iainl_liquid_b = models.FloatField(db_column='IAINL_liquid_b', blank=True, null=True)  # Field name made lowercase.
    iail_gas_a = models.FloatField(db_column='IAIL_gas_a', blank=True, null=True)  # Field name made lowercase.
    iail_gas_b = models.FloatField(db_column='IAIL_gas_b', blank=True, null=True)  # Field name made lowercase.
    iail_liquid_a = models.FloatField(db_column='IAIL_liquid_a', blank=True, null=True)  # Field name made lowercase.
    iail_liquid_b = models.FloatField(db_column='IAIL_liquid_b', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_58_ca_component_dm'
        verbose_name = "Table 5.8M – Component Damage Flammable Consequence Equation Constant"


class Tbl59ComponentDamagePerson(models.Model):
    fluid = models.TextField(db_column='Fluid', blank=True, null=True)  # Field name made lowercase.
    cainl_gas_a = models.FloatField(db_column='CAINL_gas_a', blank=True, null=True)  # Field name made lowercase.
    cainl_gas_b = models.FloatField(db_column='CAINL_gas_b', blank=True, null=True)  # Field name made lowercase.
    cainl_liquid_a = models.FloatField(db_column='CAINL_liquid_a', blank=True, null=True)  # Field name made lowercase.
    cainl_liquid_b = models.FloatField(db_column='CAINL_liquid_b', blank=True, null=True)  # Field name made lowercase.
    call_gas_a = models.FloatField(db_column='CALL_gas_a', blank=True, null=True)  # Field name made lowercase.
    call_gas_b = models.FloatField(db_column='CALL_gas_b', blank=True, null=True)  # Field name made lowercase.
    call_liquid_a = models.FloatField(db_column='CALL_liquid_a', blank=True, null=True)  # Field name made lowercase.
    call_liquid_b = models.FloatField(db_column='CALL_liquid_b', blank=True, null=True)  # Field name made lowercase.
    iainl_gas_a = models.FloatField(db_column='IAINL_gas_a', blank=True, null=True)  # Field name made lowercase.
    iainl_gas_b = models.FloatField(db_column='IAINL_gas_b', blank=True, null=True)  # Field name made lowercase.
    iainl_liquid_a = models.FloatField(db_column='IAINL_liquid_a', blank=True, null=True)  # Field name made lowercase.
    iainl_liquid_b = models.FloatField(db_column='IAINL_liquid_b', blank=True, null=True)  # Field name made lowercase.
    iail_gas_a = models.FloatField(db_column='IAIL_gas_a', blank=True, null=True)  # Field name made lowercase.
    iail_gas_b = models.FloatField(db_column='IAIL_gas_b', blank=True, null=True)  # Field name made lowercase.
    iail_liquid_a = models.FloatField(db_column='IAIL_liquid_a', blank=True, null=True)  # Field name made lowercase.
    iail_liquid_b = models.FloatField(db_column='IAIL_liquid_b', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_59_component_damage_person'
        verbose_name = "Table 5.9M – Personnel Injury Flammable Consequence Equation Constant"


class Tbl64DmLinningInorganic(models.Model):
    yearssincelastinspection = models.IntegerField(db_column='YearsSinceLastInspection', blank=True, null=True)  # Field name made lowercase.
    strip_lined_alloy = models.FloatField(db_column='Strip lined alloy', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    castable_refractory = models.FloatField(db_column='Castable refractory', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    castable_refractory_severe_condition = models.IntegerField(db_column='Castable refractory severe condition', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    glass_lined = models.IntegerField(db_column='Glass lined', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    acid_brick = models.IntegerField(db_column='Acid Brick', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibreglass = models.IntegerField(db_column='Fibreglass', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_64_dm_linning_inorganic'
        verbose_name = "Table 6.4 – Lining Damage Factors – Inorganic Lining"


class Tbl65DmLinningOrganic(models.Model):
    yearinservice = models.IntegerField(db_column='YearInService', blank=True, null=True)  # Field name made lowercase.
    morethan6years = models.IntegerField(db_column='MoreThan6Years', blank=True, null=True)  # Field name made lowercase.
    withinlast6years = models.IntegerField(db_column='WithinLast6Years', blank=True, null=True)  # Field name made lowercase.
    withinlast3years = models.FloatField(db_column='WithinLast3Years', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_65_dm_linning_organic'
        verbose_name = "Table 6.5 – Lining Damage Factors – Organic Lining"


class Tbl71PropertiesStorageTank(models.Model):
    fluid = models.TextField(db_column='Fluid', blank=True, null=True)  # Field name made lowercase.
    level_1_consequence_analysis_representative_fluid = models.TextField(db_column='Level 1 Consequence Analysis Representative Fluid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    molecular_weight = models.IntegerField(db_column='Molecular Weight', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    liquid_density = models.FloatField(db_column='Liquid Density', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    liquid_density_viscosity = models.FloatField(db_column='Liquid Density Viscosity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'tbl_71_properties_storage_tank'
        verbose_name = "Table 7.1M – Fluids and Fluid Properties for Atmospheric Storage Tank Consequence Analysi"


class Tbl74SccDmPwht(models.Model):
    svi = models.IntegerField(db_column='SVI', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    number_1d = models.IntegerField(db_column='1D', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1c = models.IntegerField(db_column='1C', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1b = models.IntegerField(db_column='1B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1a = models.IntegerField(db_column='1A', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2d = models.IntegerField(db_column='2D', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2c = models.IntegerField(db_column='2C', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2a = models.IntegerField(db_column='2A', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3d = models.IntegerField(db_column='3D', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3c = models.IntegerField(db_column='3C', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3a = models.IntegerField(db_column='3A', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4d = models.IntegerField(db_column='4D', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4c = models.IntegerField(db_column='4C', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4b = models.IntegerField(db_column='4B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4a = models.IntegerField(db_column='4A', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5d = models.IntegerField(db_column='5D', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5c = models.IntegerField(db_column='5C', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5b = models.IntegerField(db_column='5B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5a = models.IntegerField(db_column='5A', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6d = models.IntegerField(db_column='6D', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6c = models.IntegerField(db_column='6C', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6b = models.IntegerField(db_column='6B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6a = models.IntegerField(db_column='6A', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'tbl_74_scc_dm_pwht'
        verbose_name = "Table 7.4 – SCC Damage Factors – All SCC Mechanism"

class RwDamageMechanism(models.Model):
    id = models.ForeignKey(RwAssessment, on_delete=models.CASCADE, db_column='ID', primary_key=True)
    dmitemid = models.ForeignKey(DmItems, on_delete=models.CASCADE, db_column='DMItemID', primary_key=True)
    isactive = models.IntegerField(default=1, db_column='IsActive')
    notes = models.TextField(db_column='Notes', null=True)
    expectedtypeid = models.IntegerField(default=0, db_column='ExpectedTypeID')
    isel = models.IntegerField(default=0, db_column='IsEL')
    elvalue = models.IntegerField(default=0, db_column='ELValue')
    isdf = models.IntegerField(default= 1, db_column='IsDF')
    isuserdisabled = models.IntegerField(default=0, db_column='IsUserDisabled')
    df1 = models.FloatField(db_column='DF1')
    df2 = models.FloatField(db_column='DF2')
    df3 = models.FloatField(db_column='DF3')
    dfbase = models.FloatField(db_column='DFBase')
    rli = models.FloatField(db_column='RLI', default=0)
    highestinspectioneffectiveness = models.TextField(max_length=50, db_column='HighestInspectionEffectiveness')
    secondinspectioneffectiveness = models.TextField(max_length=50, db_column='SecondInspectionEffectiveness', null=True)
    numberofinspections = models.IntegerField(db_column='NumberOfInspections')
    lastinspdate = models.DateTimeField(db_column='LastInspDate', blank=True)
    inspduedate = models.DateTimeField(db_column='InspDueDate', blank=True)

    class Meta:
        managed = False
        db_table = 'rw_damage_mechanism'