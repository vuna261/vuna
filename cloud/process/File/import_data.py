import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'RbiCloud.settings'
application = get_wsgi_application()

from xlrd import open_workbook
from django.shortcuts import Http404
from cloud import models
from datetime import datetime

def checkEquipmentComponentExist(equipmentNumber,componentNumber):
    try:
        eq = models.EquipmentMaster.objects.get(equipmentnumber= equipmentNumber)
        count = models.ComponentMaster.objects.filter(equipmentid= eq.equipmentid, componentnumber= componentNumber).exists()
        return count
    except:
        return False

def checkDate(datestring):
    try:
        data = datetime.strptime(datestring, '%m-%d-%y')
        return data
    except:
        return False

def convertDate(dateString):
    try:
        return datetime.strptime(dateString, '%m-%d-%y')
    except:
        return datetime.now().date()

def convertDateInsp(dateString):
    try:
        seconds = (dateString - 25569) * 86400
        return datetime.utcfromtimestamp(seconds)
    except:
        return datetime.now().date()

def convertTF(data):
    if data == 'TRUE' or data == 'True' or data == 1:
        return 1
    else:
        return 0

def convertFloat(data):
    try:
        return float(data)
    except:
        return 0

def importInspectionPlan(filename):
    try:
        excel = open_workbook(filename)
        ws = excel.sheet_by_name('Inspections')
        rowdata = ws.nrows
        coldata = ws.ncols
        if coldata == 8:
            for row in range(1,rowdata):
                if ws.cell(row,2).value and ws.cell(row,3).value and ws.cell(row,4).value and ws.cell(row,6).value and ws.cell(row,7).value:
                    if checkEquipmentComponentExist(ws.cell(row,2).value, ws.cell(row,3).value):
                        his = models.RwInspectionHistory(inspectionplanname=ws.cell(row,0).value, inspectioncoveragename=ws.cell(row,1).value,
                                                         equipmentnumber=ws.cell(row,2).value, componentnumber=ws.cell(row,3).value,
                                                         dm=ws.cell(row,4).value, inspectiontype=ws.cell(row,5).value,
                                                         inspectiondate=convertDateInsp(ws.cell(row,6).value),
                                                         inspectioneffective=ws.cell(row,7).value)
                        his.save()

    except:
        raise Http404

# --------------COUNT SHEET COL-------------
#  Worksheet | PlantProcess | StorageTank
# 	0			32				36
# 	1			32				24
# 	2			18				18
# 	3			22				25
# 	4			22				18
# 	5			15				15
# ------------------------------------------

# kiem tra dieu kien thoa man va dieu kien ton tai cua du lieu
def checkFacilityAvaiable(site, facility):
    try:
        site = models.Sites.objects.get(sitename= site)
        if models.Facility.objects.filter(facilityname= facility, siteid=site.siteid).exists():
            return True
        else:
            return False
    except:
        return False

def checkEquipmentAvaiable(site,facility,equipmentnumber, equipmentName):
    try:
        site = models.Sites.objects.get(sitename= site)
        faci = models.Facility.objects.get(facilityname= facility)
        countE = models.EquipmentMaster.objects.filter(equipmentnumber= equipmentnumber ,siteid= site.siteid, facilityid=faci.facilityid).exists()
        avaiE = models.EquipmentMaster.objects.filter(equipmentnumber=equipmentnumber).exists()
        if ( countE or not avaiE ) and equipmentName :
            return True
        else:
            return False
    except:
        return False

def checkComponentAvaiable(equipmentnumber, componentnumber):
    try:
        equ = models.EquipmentMaster.objects.get(equipmentnumber= equipmentnumber)
        countComp = models.ComponentMaster.objects.filter(componentnumber= componentnumber, equipmentid= equ.equipmentid).exists()
        avaiComp = models.ComponentMaster.objects.filter(componentnumber= componentnumber).exists()
        if countComp or not avaiComp:
            return True
        else:
            return False
    except:
        return False

def checkFacilityExist(facilityname):
    existF = models.Facility.objects.filter(facilityname= facilityname).exists()
    return existF

def checkEquipmentExist(equipmentNumber):
    existE = models.EquipmentMaster.objects.filter(equipmentnumber= equipmentNumber).exists()
    return existE

def checkComponentExist(componentNumber):
    existC = models.ComponentMaster.objects.filter(componentnumber= componentNumber).exists()
    return existC

def checkDesigncodeAvaiable(designcode, sitename):
    try:
        site = models.Sites.objects.get(sitename= sitename)
        avaiDesign = models.DesignCode.objects.filter(designcode= designcode, siteid= site.siteid).exists()
        design = models.DesignCode.objects.filter(designcode= designcode).exists()
        if avaiDesign or not design:
            return True
        else:
            return False
    except:
        return False

def checkDesigncodeExist(designcode):
    existDesign = models.DesignCode.objects.filter(designcode= designcode).exists()
    return existDesign

def checkManufactureExist(manufacturename):
    existManu = models.Manufacturer.objects.filter(manufacturername= manufacturename).exists()
    return existManu

def checkManufactureAvaiable(manufacture, sitename):
    try:
        site = models.Sites.objects.get(sitename= sitename)
        avaiManufacture = models.Manufacturer.objects.filter(manufacturername= manufacture, siteid= site.siteid).exists()
        existManu = models.Manufacturer.objects.filter(manufacturername= manufacture).exists()
        if avaiManufacture or not existManu:
            return True
        else:
            return False
    except:
        return False

def checkSiteAvaiable(sitename):
    existSite = models.Sites.objects.filter(sitename= sitename).exists()
    return existSite

def getSiteID(sitename):
    return models.Sites.objects.get(sitename= sitename).siteid

def getFacilityID(facilityname):
    return models.Facility.objects.get(facilityname=facilityname).facilityid

def getEquipmentTypeID(equipmentTypeName):
    equipmentType = models.EquipmentType.objects.get(equipmenttypename= equipmentTypeName)
    return equipmentType.equipmenttypeid

def getComponentTypeID(componentTypeName):
    componentType = models.ComponentType.objects.get(componenttypename= componentTypeName)
    return componentType.componenttypeid

def getApiComponentTypeID(apicomponentType):
    api = models.ApiComponentType.objects.get(apicomponenttypename= apicomponentType)
    return api.apicomponenttypeid

def getDesigncodeID(designcode):
    return models.DesignCode.objects.get(designcode=designcode).designcodeid

def getManufactureID(manufacture):
    return models.Manufacturer.objects.get(manufacturername= manufacture).manufacturerid

def getEquipmentID(equipmentNumber):
    return models.EquipmentMaster.objects.get(equipmentnumber= equipmentNumber).equipmentid

def getComponentID(componentNumber):
    return models.ComponentMaster.objects.get(componentnumber=componentNumber).componentid

def getApiTankFluid(fluidname):
    if fluidname == "Gasoline":
        return "C6-C8"
    elif fluidname == "Light Diesel Oil":
        return "C9-C12"
    elif fluidname == "Heavy Diesel Oil":
        return "C13-C16"
    elif fluidname == "Fuel Oil" or fluidname == "Crude Oil":
        return "C17-C25"
    else:
        return "C25+"

#sheet 0
def processEquipmentMaster(ws):
    try:
        ncol = ws.ncols
        nrow = ws.nrows
        if ncol == 32:
            for row in range(1, nrow):
                if ws.cell(row, 0).value and ws.cell(row, 1).value and ws.cell(row, 2).value and ws.cell(row,
                                                                                                             3).value and ws.cell(
                        row, 4).value and ws.cell(row, 5).value and ws.cell(row, 6).value and ws.cell(row, 7).value:
                    if checkSiteAvaiable(ws.cell(row, 4).value):
                        if checkFacilityAvaiable(ws.cell(row, 4).value, ws.cell(row, 5).value):
                            if checkFacilityExist(ws.cell(row, 5).value):
                                fc = models.Facility.objects.get(facilityname=ws.cell(row, 5).value)
                                try:
                                    managefactor = float(ws.cell(row, 31).value)
                                except:
                                    managefactor = 0.1
                                fc.managementfactor = managefactor
                                fc.save()

                        if checkDesigncodeAvaiable(ws.cell(row, 3).value, ws.cell(row, 4).value):
                            if not checkDesigncodeExist(ws.cell(row, 3).value):
                                ds = models.DesignCode(designcode=ws.cell(row, 3).value, designcodeapp='None',
                                                       siteid_id=getSiteID(ws.cell(row, 4).value))
                                ds.save()

                        if checkManufactureAvaiable(ws.cell(row, 6).value, ws.cell(row, 4).value):
                            if not checkManufactureExist(ws.cell(row, 6).value):
                                mn = models.Manufacturer(manufacturername=ws.cell(row, 6).value,
                                                         siteid_id=getSiteID(ws.cell(row, 4).value))
                                mn.save()

                        if checkEquipmentAvaiable(ws.cell(row, 4).value, ws.cell(row, 5).value,ws.cell(row,0).value, ws.cell(row, 2).value):
                            if checkEquipmentExist(ws.cell(row, 0).value):
                                eq = models.EquipmentMaster.objects.get(equipmentnumber=ws.cell(row, 0).value)
                                eq.equipmenttypeid_id = getEquipmentTypeID(ws.cell(row, 1).value)
                                eq.equipmentname = ws.cell(row, 2).value
                                eq.commissiondate = convertDateInsp(ws.cell(row, 7).value)
                                eq.designcodeid_id = getDesigncodeID(ws.cell(row, 3).value)
                                eq.siteid_id = getSiteID(ws.cell(row, 4).value)
                                eq.facilityid_id = getFacilityID(ws.cell(row, 5).value)
                                eq.manufacturerid_id = getManufactureID(ws.cell(row, 6).value)
                                eq.pfdno = ws.cell(row, 8).value
                                eq.processdescription = ws.cell(row, 9).value
                                eq.equipmentdesc = ws.cell(row, 10).value
                                eq.save()
                            else:
                                eq = models.EquipmentMaster(equipmentnumber= ws.cell(row,0).value, equipmenttypeid_id= getEquipmentTypeID(ws.cell(row, 1).value),
                                                            equipmentname= ws.cell(row,2).value, commissiondate = convertDateInsp(ws.cell(row, 7).value),
                                                            designcodeid_id=getDesigncodeID(ws.cell(row, 3).value), siteid_id = getSiteID(ws.cell(row, 4).value),
                                                            facilityid_id=getFacilityID(ws.cell(row, 5).value), manufacturerid_id = getManufactureID(ws.cell(row, 6).value),
                                                            pfdno=ws.cell(row, 8).value, processdescription = ws.cell(row, 9).value, equipmentdesc = ws.cell(row, 10).value)
                                eq.save()
        elif ncol == 36:
            for row in range(1, nrow):
                if ws.cell(row, 0).value and ws.cell(row, 1).value and ws.cell(row, 2).value and ws.cell(row,
                                                                                                             3).value and ws.cell(
                        row, 4).value and ws.cell(row, 5).value and ws.cell(row, 6).value and ws.cell(row, 7).value:
                    if checkSiteAvaiable(ws.cell(row, 4).value):
                        if checkFacilityAvaiable(ws.cell(row, 4).value, ws.cell(row, 5).value):
                            if checkFacilityExist(ws.cell(row, 5).value):
                                fc = models.Facility.objects.get(facilityname=ws.cell(row, 5).value)
                                try:
                                    managefactor = float(ws.cell(row, 29).value)
                                except:
                                    managefactor = 0.1
                                fc.managementfactor = managefactor
                                fc.save()

                        if checkDesigncodeAvaiable(ws.cell(row, 3).value, ws.cell(row, 4).value):
                            if not checkDesigncodeExist(ws.cell(row, 3).value):
                                ds = models.DesignCode(designcode=ws.cell(row, 3).value, designcodeapp='None',
                                                       siteid_id=getSiteID(ws.cell(row, 4).value))
                                ds.save()

                        if checkManufactureAvaiable(ws.cell(row, 6).value, ws.cell(row, 4).value):
                            if not checkManufactureExist(ws.cell(row, 6).value):
                                mn = models.Manufacturer(manufacturername=ws.cell(row, 6).value,
                                                         siteid_id=getSiteID(ws.cell(row, 4).value))
                                mn.save()

                        if checkEquipmentAvaiable(ws.cell(row, 4).value, ws.cell(row, 5).value,ws.cell(row,0).value , ws.cell(row, 2).value):
                            if checkEquipmentExist(ws.cell(row, 0).value):
                                eq = models.EquipmentMaster.objects.get(equipmentnumber=ws.cell(row, 0).value)
                                eq.equipmenttypeid_id = getEquipmentTypeID(ws.cell(row, 1).value)
                                eq.equipmentname = ws.cell(row, 2).value
                                eq.commissiondate = convertDateInsp(ws.cell(row, 7).value)
                                eq.designcodeid_id = getDesigncodeID(ws.cell(row, 3).value)
                                eq.siteid_id = getSiteID(ws.cell(row, 4).value)
                                eq.facilityid_id = getFacilityID(ws.cell(row, 5).value)
                                eq.manufacturerid_id = getManufactureID(ws.cell(row, 6).value)
                                eq.pfdno = ws.cell(row, 8).value
                                eq.processdescription = ws.cell(row, 9).value
                                eq.equipmentdesc = ws.cell(row, 10).value
                                eq.save()
                            else:
                                eq = models.EquipmentMaster(equipmentnumber= ws.cell(row,0).value, equipmenttypeid_id= getEquipmentTypeID(ws.cell(row, 1).value),
                                                            equipmentname= ws.cell(row,2).value, commissiondate = convertDateInsp(ws.cell(row, 7).value),
                                                            designcodeid_id=getDesigncodeID(ws.cell(row, 3).value), siteid_id = getSiteID(ws.cell(row, 4).value),
                                                            facilityid_id=getFacilityID(ws.cell(row, 5).value), manufacturerid_id = getManufactureID(ws.cell(row, 6).value),
                                                            pfdno=ws.cell(row, 8).value, processdescription = ws.cell(row, 9).value, equipmentdesc = ws.cell(row, 10).value)
                                eq.save()
        # neu k phai format tren thi bo qua. k thuc hien
    except Exception as e:
        print('Exception at Equipment Master Excel')
        print(e)

#sheet 1
def processComponentMaster(ws):
    try:
        ncol = ws.ncols
        nrow = ws.nrows
        if ncol == 32 or ncol == 24:
            for row in range(1,nrow):
                if ws.cell(row,0).value and ws.cell(row,1).value and ws.cell(row,2).value and ws.cell(row,3).value and ws.cell(row,4).value and ws.cell(row,7).value:
                    if checkComponentAvaiable(ws.cell(row,0).value, ws.cell(row,1).value):
                        if checkComponentExist(ws.cell(row,1).value):
                            comp = models.ComponentMaster.objects.get(componentnumber= ws.cell(row,1).value)
                            comp.componenttypeid_id = getComponentTypeID(ws.cell(row,2).value)
                            comp.componentname = ws.cell(row,4).value
                            comp.componentdesc = ws.cell(row,6).value
                            comp.isequipmentlinked = convertTF(ws.cell(row,5).value)
                            comp.apicomponenttypeid = getApiComponentTypeID(ws.cell(row,3).value)
                            comp.save()
                        else:
                            comp = models.ComponentMaster(componentnumber= ws.cell(row,1).value, componenttypeid_id= getComponentTypeID(ws.cell(row,2).value),
                                                          componentname= ws.cell(row,4).value, componentdesc= ws.cell(row,6).value,equipmentid_id = getEquipmentID(ws.cell(row,0).value),
                                                          isequipmentlinked=convertTF(ws.cell(row,5).value), apicomponenttypeid = getApiComponentTypeID(ws.cell(row,3).value))
                            comp.save()
    except Exception as e:
        print("Exception at Component Master Excel")
        print(e)

listProposal = []
#sheet 1
def processAssessment(ws):
    try:
        ncol = ws.ncols
        nrow = ws.nrows
        if ncol == 32:
            for row in range(1,nrow):
                if ws.cell(row, 0).value and ws.cell(row, 1).value and ws.cell(row, 2).value and ws.cell(row,
                                                                                                         3).value and ws.cell(
                    row, 4).value and ws.cell(row, 7).value:
                    if checkComponentAvaiable(ws.cell(row, 0).value, ws.cell(row, 1).value):
                        rwAss = models.RwAssessment(equipmentid_id= getEquipmentID(ws.cell(row,0).value), componentid_id= getComponentID(ws.cell(row,1).value),
                                                    assessmentdate= convertDateInsp(ws.cell(row,7).value), riskanalysisperiod= 36,
                                                    isequipmentlinked= convertTF(ws.cell(row,5).value), proposalname= "New Excel Proposal " + str(datetime.now().strftime('%m-%d-%y')))
                        rwAss.save()

                        #Luu lai cac bang trung gian
                        rwEquip = models.RwEquipment(id= rwAss, commissiondate= datetime.now())
                        rwEquip.save()

                        rwComp = models.RwComponent(id = rwAss)
                        rwComp.save()

                        rwExco = models.RwExtcorTemperature(id = rwAss)
                        rwExco.save()

                        rwStream = models.RwStream(id= rwAss)
                        rwStream.save()

                        rwMater = models.RwMaterial(id= rwAss)
                        rwMater.save()

                        rwCoat = models.RwCoating(id= rwAss, externalcoatingdate= datetime.now())
                        rwCoat.save()

                        rwInputCa = models.RwInputCaLevel1(id = rwAss)
                        rwInputCa.save()

                        listProposal.append(rwAss)
        elif ncol == 24:
            for row in range(1, nrow):
                if ws.cell(row, 0).value and ws.cell(row, 1).value and ws.cell(row, 2).value and ws.cell(row,
                                                                                                         3).value and ws.cell(
                    row, 4).value and ws.cell(row, 7).value:
                    if checkComponentAvaiable(ws.cell(row, 0).value, ws.cell(row, 1).value):
                        rwAss = models.RwAssessment(equipmentid_id=getEquipmentID(ws.cell(row, 0).value),
                                                    componentid_id=getComponentID(ws.cell(row, 1).value),
                                                    assessmentdate=convertDateInsp(ws.cell(row, 7).value),
                                                    riskanalysisperiod=36,
                                                    isequipmentlinked=convertTF(ws.cell(row, 5).value),
                                                    proposalname="New Excel Proposal " + str(
                                                        datetime.now().strftime('%m-%d-%y')))
                        rwAss.save()

                        # Luu lai cac bang trung gian
                        rwEquip = models.RwEquipment(id=rwAss, commissiondate= datetime.now())
                        rwEquip.save()

                        rwComp = models.RwComponent(id=rwAss)
                        rwComp.save()

                        rwExco = models.RwExtcorTemperature(id=rwAss)
                        rwExco.save()

                        rwStream = models.RwStream(id=rwAss)
                        rwStream.save()

                        rwMater = models.RwMaterial(id=rwAss)
                        rwMater.save()

                        rwCoat = models.RwCoating(id=rwAss, externalcoatingdate= datetime.now())
                        rwCoat.save()

                        rwInputTank = models.RwInputCaTank(id= rwAss)
                        rwInputTank.save()

                        listProposal.append(rwAss)
    except Exception as e:
        print("Exception at Assessment")
        print(e)

#sheet 0
def processRwEquipment(ws):
    try:
        ncol = ws.ncols
        nrow = ws.nrows
        if ncol == 32:
            for row in range(1,nrow):
                if ws.cell(row, 0).value and ws.cell(row, 1).value and ws.cell(row, 2).value and ws.cell(row,
                                                                                                         3).value and ws.cell(
                    row, 4).value and ws.cell(row, 5).value and ws.cell(row, 6).value and ws.cell(row, 7).value:
                    if checkEquipmentAvaiable(ws.cell(row, 4).value, ws.cell(row, 5).value,ws.cell(row,0).value, ws.cell(row, 2).value):
                        for a in listProposal:
                            if a.equipmentid_id == getEquipmentID(ws.cell(row,0).value):
                                rwEq = models.RwEquipment.objects.get(id=a.id)
                                rwEq.commissiondate = convertDateInsp(ws.cell(row,7).value)
                                rwEq.adminupsetmanagement = convertTF(ws.cell(row,11).value)
                                rwEq.containsdeadlegs= convertTF(ws.cell(row,12).value)
                                rwEq.cyclicoperation= convertTF(ws.cell(row,14).value)
                                rwEq.highlydeadleginsp= convertTF(ws.cell(row,13).value)
                                rwEq.downtimeprotectionused= convertTF(ws.cell(row,15).value)
                                if ws.cell(row,27).value:
                                    rwEq.externalenvironment = ws.cell(row,27).value
                                rwEq.heattraced = convertTF(ws.cell(row,17).value)
                                rwEq.interfacesoilwater = convertTF(ws.cell(row,19).value)
                                rwEq.lineronlinemonitoring = convertTF(ws.cell(row,24).value)
                                rwEq.materialexposedtoclext = convertTF(ws.cell(row,23).value)
                                rwEq.minreqtemperaturepressurisation= convertFloat(ws.cell(row,21).value)
                                if ws.cell(row,29).value:
                                    rwEq.onlinemonitoring = ws.cell(row,29).value
                                rwEq.presencesulphideso2 = convertTF(ws.cell(row,25).value)
                                rwEq.presencesulphideso2shutdown = convertTF(ws.cell(row,26).value)
                                rwEq.pressurisationcontrolled = convertTF(ws.cell(row,20).value)
                                rwEq.pwht = convertTF(ws.cell(row,18).value)
                                rwEq.steamoutwaterflush = convertTF(ws.cell(row,16).value)
                                try:
                                    rwEq.managementfactor = float(ws.cell(row,31).value)
                                except:
                                    rwEq.managementfactor = 0.1
                                if ws.cell(row,28).value:
                                    rwEq.thermalhistory = ws.cell(row,28).value
                                rwEq.yearlowestexptemp = convertTF(ws.cell(row,22).value)
                                rwEq.volume = convertFloat(ws.cell(row, 30).value)
                                rwEq.save()
        elif ncol == 36:
            for row in range(1,nrow):
                if ws.cell(row, 0).value and ws.cell(row, 1).value and ws.cell(row, 2).value and ws.cell(row,
                                                                                                         3).value and ws.cell(
                    row, 4).value and ws.cell(row, 5).value and ws.cell(row, 6).value and ws.cell(row, 7).value:
                    if checkEquipmentAvaiable(ws.cell(row, 4).value, ws.cell(row, 5).value,ws.cell(row,0).value, ws.cell(row, 2).value):
                        for a in listProposal:
                            if a.equipmentid_id == getEquipmentID(ws.cell(row,0).value):
                                rwEq = models.RwEquipment.objects.get(id= a.id)
                                rwInputCaTank = models.RwInputCaTank.objects.get(id= a.id)
                                rwEq.commissiondate = convertDateInsp(ws.cell(row,7).value)
                                rwEq.adminupsetmanagement = convertTF(ws.cell(row,11).value)
                                rwEq.cyclicoperation = convertTF(ws.cell(row,12).value)
                                rwEq.downtimeprotectionused = convertTF(ws.cell(row,13).value)
                                rwEq.steamoutwaterflush = convertTF(ws.cell(row,14).value)
                                rwEq.heattraced = convertTF(ws.cell(row,15).value)
                                rwEq.pwht = convertTF(ws.cell(row,16).value)
                                rwEq.interfacesoilwater = convertTF(ws.cell(row,17).value)
                                rwEq.pressurisationcontrolled = convertTF(ws.cell(row,18).value)
                                rwEq.minreqtemperaturepressurisation = convertFloat(ws.cell(row,19).value)
                                rwEq.yearlowestexptemp = convertTF(ws.cell(row,20).value)
                                rwEq.materialexposedtoclext = convertTF(ws.cell(row,21).value)
                                rwEq.lineronlinemonitoring = convertTF(ws.cell(row,22).value)
                                rwEq.presencesulphideso2 = convertTF(ws.cell(row,23).value)
                                rwEq.presencesulphideso2shutdown = convertTF(ws.cell(row,24).value)
                                if ws.cell(row,25).value:
                                    rwEq.externalenvironment = ws.cell(row,25).value
                                if ws.cell(row,26).value:
                                    rwEq.thermalhistory = ws.cell(row,26).value
                                if ws.cell(row,27).value:
                                    rwEq.onlinemonitoring = ws.cell(row,27).value
                                rwEq.volume = convertFloat(ws.cell(row,28).value)
                                try:
                                    rwEq.managementfactor = float(ws.cell(row,29).value)
                                except:
                                    rwEq.managementfactor = 0.1
                                if ws.cell(row,30).value:
                                    rwEq.typeofsoil = ws.cell(row,30).value
                                    rwInputCaTank.soil_type = ws.cell(row,30).value
                                rwEq.distancetogroundwater = convertFloat(ws.cell(row,31).value)
                                if ws.cell(row,32).value:
                                    rwEq.environmentsensitivity = ws.cell(row,32).value
                                    rwInputCaTank.environ_sensitivity = ws.cell(row,32).value
                                if ws.cell(row,33).value:
                                    rwEq.adjustmentsettle = ws.cell(row,33).value
                                rwEq.componentiswelded = convertTF(ws.cell(row,34).value)
                                rwEq.tankismaintained = convertTF(ws.cell(row,35).value)

                                rwInputCaTank.sw = convertFloat(ws.cell(row, 31).value)
                                rwEq.save()
                                rwInputCaTank.save()
    except Exception as e:
        print("Exception RwEquipment")
        print(e)

#sheet 1
def processRwComponent(ws):
    try:
        ncol = ws.ncols
        nrow = ws.nrows
        if ncol == 32:
            for row in range(1, nrow):
                if ws.cell(row, 0).value and ws.cell(row, 1).value and ws.cell(row, 2).value and ws.cell(row,
                                                                                                         3).value and ws.cell(
                    row, 4).value and ws.cell(row, 7).value:
                    if checkComponentAvaiable(ws.cell(row, 0).value, ws.cell(row, 1).value):
                        for a in listProposal:
                            if a.componentid_id == getComponentID(ws.cell(row, 1).value):
                                rwCom = models.RwComponent.objects.get(id= a.id)
                                rwCom.nominaldiameter = convertFloat(ws.cell(row,9).value)
                                rwCom.nominalthickness = convertFloat(ws.cell(row,10).value)
                                rwCom.currentthickness = convertFloat(ws.cell(row,11).value)
                                rwCom.minreqthickness = convertFloat(ws.cell(row,12).value)
                                rwCom.currentcorrosionrate = convertFloat(ws.cell(row,13).value)
                                if ws.cell(row,23).value:
                                    rwCom.branchdiameter = ws.cell(row,23).value
                                if ws.cell(row,24).value:
                                    rwCom.branchjointtype = ws.cell(row,24).value
                                if ws.cell(row,20).value:
                                    rwCom.brinnelhardness = ws.cell(row,20).value
                                rwCom.chemicalinjection = convertTF(ws.cell(row,17).value)
                                rwCom.highlyinjectioninsp = convertTF(ws.cell(row,19).value)
                                if ws.cell(row,21).value:
                                    rwCom.complexityprotrusion = ws.cell(row,21).value
                                if ws.cell(row,31).value:
                                    rwCom.correctiveaction = ws.cell(row,31).value
                                rwCom.crackspresent = convertTF(ws.cell(row,16).value)
                                if ws.cell(row,22).value:
                                    rwCom.cyclicloadingwitin15_25m = ws.cell(row,22).value
                                rwCom.damagefoundinspection = convertTF(ws.cell(row,15).value)
                                rwCom.deltafatt = convertFloat(ws.cell(row,14).value)
                                if ws.cell(row,25).value:
                                    rwCom.numberpipefittings = ws.cell(row,25).value
                                if ws.cell(row,26).value:
                                    rwCom.pipecondition = ws.cell(row,26).value
                                if ws.cell(row,27).value:
                                    rwCom.previousfailures = ws.cell(row,27).value
                                if ws.cell(row,29).value:
                                    rwCom.shakingamount = ws.cell(row,29).value
                                rwCom.shakingdetected = convertTF(ws.cell(row,28).value)
                                if ws.cell(row,30).value:
                                    rwCom.shakingtime = ws.cell(row,30).value
                                rwCom.trampelements = convertTF(ws.cell(row,18).value)
                                rwCom.save()
        elif ncol == 24:
            for row in range(1, nrow):
                if ws.cell(row, 0).value and ws.cell(row, 1).value and ws.cell(row, 2).value and ws.cell(row,
                                                                                                         3).value and ws.cell(
                    row, 4).value and ws.cell(row, 7).value:
                    if checkComponentAvaiable(ws.cell(row, 0).value, ws.cell(row, 1).value):
                        for a in listProposal:
                            if a.componentid_id == getComponentID(ws.cell(row, 1).value):
                                rwCom = models.RwComponent.objects.get(id= a.id)
                                rwInputCaTank = models.RwInputCaTank.objects.get(id= a.id)
                                rwCom.nominaldiameter = convertFloat(ws.cell(row,9).value)
                                rwInputCaTank.tank_diametter = convertFloat(ws.cell(row,9).value)
                                rwCom.nominalthickness = convertFloat(ws.cell(row,10).value)
                                rwCom.currentthickness = convertFloat(ws.cell(row,11).value)
                                rwCom.minreqthickness = convertFloat(ws.cell(row,12).value)
                                rwCom.currentcorrosionrate = convertFloat(ws.cell(row,13).value)
                                if ws.cell(row,18).value:
                                    rwCom.brinnelhardness = ws.cell(row,18).value
                                if ws.cell(row,19).value:
                                    rwCom.complexityprotrusion = ws.cell(row,19).value
                                if ws.cell(row,20).value:
                                    rwCom.severityofvibration = ws.cell(row,20).value
                                rwCom.releasepreventionbarrier = convertTF(ws.cell(row,21).value)
                                rwInputCaTank.prevention_barrier = convertTF(ws.cell(row,21).value)
                                rwCom.concretefoundation = convertTF(ws.cell(row,22).value)
                                rwCom.shellheight = convertFloat(ws.cell(row,23).value)
                                rwInputCaTank.shell_course_height = convertFloat(ws.cell(row,23).value)
                                rwCom.crackspresent = convertTF(ws.cell(row,16).value)
                                rwCom.damagefoundinspection = convertTF(ws.cell(row,15).value)
                                rwCom.deltafatt = convertFloat(ws.cell(row,14).value)
                                rwCom.trampelements = convertTF(ws.cell(row,17).value)
                                rwCom.save()
                                rwInputCaTank.save()
    except Exception as e:
        print("Exception at RwComponent")
        print(e)

#sheet 2
def processRwExtcor(ws):
    try:
        ncol = ws.ncols
        nrow = ws.nrows
        if ncol == 18:
            for row in range(1,nrow):
                if ws.cell(row,0).value:
                    for a in listProposal:
                        if a.componentid_id == getComponentID(ws.cell(row,0).value):
                            rwExt = models.RwExtcorTemperature.objects.get(id= a.id)
                            rwExt.minus12tominus8 = convertFloat(ws.cell(row,8).value)
                            rwExt.minus8toplus6 = convertFloat(ws.cell(row,9).value)
                            rwExt.plus6toplus32 = convertFloat(ws.cell(row,10).value)
                            rwExt.plus32toplus71 = convertFloat(ws.cell(row,11).value)
                            rwExt.plus71toplus107 = convertFloat(ws.cell(row,12).value)
                            rwExt.plus107toplus121 = convertFloat(ws.cell(row,13).value)
                            rwExt.plus121toplus135 = convertFloat(ws.cell(row,14).value)
                            rwExt.plus135toplus162 = convertFloat(ws.cell(row,15).value)
                            rwExt.plus162toplus176 = convertFloat(ws.cell(row,16).value)
                            rwExt.morethanplus176 = convertFloat(ws.cell(row,17).value)
                            rwExt.save()
    except Exception as e:
        print("Exception at RwExtcor")
        print(e)

#sheet 2
def processStream1(ws):
    try:
        ncol = ws.ncols
        nrow = ws.nrows
        if ncol == 18:
            for row in range(1, nrow):
                if ws.cell(row,0).value:
                    for a in listProposal:
                        if a.componentid_id == getComponentID(ws.cell(row,0).value):
                            rwStream = models.RwStream.objects.get(id= a.id)
                            rwStream.maxoperatingtemperature = convertFloat(ws.cell(row,1).value)
                            rwStream.minoperatingtemperature = convertFloat(ws.cell(row,2).value)
                            rwStream.criticalexposuretemperature = convertFloat(ws.cell(row,3).value)
                            rwStream.maxoperatingpressure = convertFloat(ws.cell(row,4).value)
                            rwStream.minoperatingpressure = convertFloat(ws.cell(row,5).value)
                            rwStream.h2spartialpressure = convertFloat(ws.cell(row,6).value)
                            rwStream.save()
    except Exception as e:
        print("Exception at RwStream sheet 2")
        print(e)

#sheet 3
def processStream2(ws):
    try:
        ncol = ws.ncols
        nrow = ws.nrows
        if ncol == 22:
            for row in range(1,nrow):
                if ws.cell(row,0).value:
                    for a in listProposal:
                        if a.componentid_id == getComponentID(ws.cell(row,0).value):
                            rwStream = models.RwStream.objects.get(id=a.id)
                            rwStream.naohconcentration = convertFloat(ws.cell(row,3).value)
                            rwStream.releasefluidpercenttoxic = convertFloat(ws.cell(row,4).value)
                            rwStream.chloride = convertFloat(ws.cell(row,5).value)
                            rwStream.co3concentration = convertFloat(ws.cell(row,6).value)
                            rwStream.h2sinwater = convertFloat(ws.cell(row,7).value)
                            rwStream.waterph = convertFloat(ws.cell(row,8).value)
                            rwStream.exposedtogasamine = convertTF(ws.cell(row,9).value)
                            rwStream.toxicconstituent = convertTF(ws.cell(row,10).value)
                            if ws.cell(row,11).value:
                                rwStream.exposuretoamine = ws.cell(row,11).value
                            if ws.cell(row,12).value:
                                rwStream.aminesolution = ws.cell(row,12).value
                            rwStream.aqueousoperation = convertTF(ws.cell(row,13).value)
                            rwStream.aqueousshutdown = convertTF(ws.cell(row,14).value)
                            rwStream.h2s = convertTF(ws.cell(row,15).value)
                            rwStream.hydrofluoric = convertTF(ws.cell(row,16).value)
                            rwStream.cyanide = convertTF(ws.cell(row,17).value)
                            rwStream.hydrogen = convertTF(ws.cell(row,18).value)
                            rwStream.caustic = convertTF(ws.cell(row,19).value)
                            rwStream.exposedtosulphur = convertTF(ws.cell(row,20).value)
                            rwStream.materialexposedtoclint = convertTF(ws.cell(row,21).value)
                            rwStream.save()
        elif ncol == 25:
            for row in range(1,nrow):
                if ws.cell(row,0).value and ws.cell(row,20).value:
                    for a in listProposal:
                        if a.componentid_id == getComponentID(ws.cell(row,0).value):
                            rwStream = models.RwStream.objects.get(id= a.id)
                            rwInputCaTank = models.RwInputCaTank.objects.get(id= a.id)
                            rwStream.naohconcentration = convertFloat(ws.cell(row,1).value)
                            rwStream.releasefluidpercenttoxic = convertFloat(ws.cell(row,2).value)
                            rwStream.chloride = convertFloat(ws.cell(row,3).value)
                            rwStream.co3concentration = convertFloat(ws.cell(row,4).value)
                            rwStream.h2sinwater = convertFloat(ws.cell(row,5).value)
                            rwStream.waterph = convertFloat(ws.cell(row,6).value)
                            rwStream.exposedtogasamine = convertTF(ws.cell(row,7).value)
                            rwStream.toxicconstituent = convertTF(ws.cell(row,8).value)
                            if ws.cell(row,9).value:
                                rwStream.exposuretoamine = ws.cell(row,9).value
                            if ws.cell(row,10).value:
                                rwStream.aminesolution = ws.cell(row,10).value
                            rwStream.aqueousoperation = convertTF(ws.cell(row,11).value)
                            rwStream.aqueousshutdown = convertTF(ws.cell(row,12).value)
                            rwStream.h2s = convertTF(ws.cell(row,13).value)
                            rwStream.hydrofluoric = convertTF(ws.cell(row,14).value)
                            rwStream.cyanide = convertTF(ws.cell(row,15).value)
                            rwStream.hydrogen = convertTF(ws.cell(row,16).value)
                            rwStream.caustic = convertTF(ws.cell(row,17).value)
                            rwStream.exposedtosulphur = convertTF(ws.cell(row,18).value)
                            rwStream.materialexposedtoclint = convertTF(ws.cell(row,19).value)
                            if ws.cell(row,20).value:
                                rwStream.tankfluidname = ws.cell(row,20).value
                                rwInputCaTank.tank_fluid = ws.cell(row,20).value
                            rwStream.fluidheight = convertFloat(ws.cell(row,21).value)
                            rwStream.fluidleavedikepercent = convertFloat(ws.cell(row,22).value)
                            rwStream.fluidleavedikeremainonsitepercent = convertFloat(ws.cell(row,23).value)
                            rwStream.fluidgooffsitepercent = convertFloat(ws.cell(row,24).value)

                            rwInputCaTank.fluid_height = convertFloat(ws.cell(row, 21).value)
                            rwInputCaTank.p_lvdike = convertFloat(ws.cell(row,22).value)
                            rwInputCaTank.p_onsite = convertFloat(ws.cell(row,23).value)
                            rwInputCaTank.p_offsite = convertFloat(ws.cell(row,24).value)
                            rwInputCaTank.api_fluid = getApiTankFluid(ws.cell(row,20).value)
                            rwStream.save()
                            rwInputCaTank.save()
    except Exception as e:
        print("Exception at RwStream sheet 3")
        print(e)

#sheet 4
def processMaterial(ws):
    try:
        ncol = ws.ncols
        nrow = ws.nrows
        if ncol == 22:
            for row in range(1, nrow):
                if ws.cell(row,0).value:
                    for a in listProposal:
                        if a.componentid_id == getComponentID(ws.cell(row,0).value):
                            rwMaterial = models.RwMaterial.objects.get(id= a.id)
                            rwMaterial.materialname = ws.cell(row,1).value
                            rwMaterial.designpressure = convertFloat(ws.cell(row,2).value)
                            rwMaterial.designtemperature = convertFloat(ws.cell(row,3).value)
                            rwMaterial.mindesigntemperature = convertFloat(ws.cell(row,4).value)
                            rwMaterial.referencetemperature = convertFloat(ws.cell(row,5).value)
                            rwMaterial.brittlefracturethickness = convertFloat(ws.cell(row,6).value)
                            rwMaterial.allowablestress = convertFloat(ws.cell(row,7).value)
                            rwMaterial.corrosionallowance = convertFloat(ws.cell(row,8).value)
                            rwMaterial.sigmaphase = convertFloat(ws.cell(row,9).value)
                            rwMaterial.carbonlowalloy = convertTF(ws.cell(row,10).value)
                            rwMaterial.austenitic = convertTF(ws.cell(row,11).value)
                            rwMaterial.temper = convertTF(ws.cell(row,12).value)
                            rwMaterial.nickelbased = convertTF(ws.cell(row,13).value)
                            rwMaterial.chromemoreequal12 = convertTF(ws.cell(row,14).value)
                            if ws.cell(row,15).value:
                                rwMaterial.sulfurcontent = ws.cell(row,15).value
                            if ws.cell(row,16).value:
                                rwMaterial.heattreatment = ws.cell(row,16).value
                            rwMaterial.ishtha = convertTF(ws.cell(row,17).value)
                            if ws.cell(row,18).value:
                                rwMaterial.hthamaterialcode = ws.cell(row,18).value
                            rwMaterial.ispta = convertTF(ws.cell(row,19).value)
                            if ws.cell(row,20).value:
                                rwMaterial.ptamaterialcode = ws.cell(row,20).value
                            rwMaterial.costfactor = convertFloat(ws.cell(row,21).value)
                            rwMaterial.save()
        elif ncol == 18:
            for row in range(1,nrow):
                if ws.cell(row,0).value:
                    for a in listProposal:
                        if a.componentid_id == getComponentID(ws.cell(row,0).value):
                            rwMaterial = models.RwMaterial.objects.get(id=a.id)
                            rwMaterial.materialname = ws.cell(row, 1).value
                            rwMaterial.designpressure = convertFloat(ws.cell(row, 2).value)
                            rwMaterial.designtemperature = convertFloat(ws.cell(row, 3).value)
                            rwMaterial.mindesigntemperature = convertFloat(ws.cell(row, 4).value)
                            rwMaterial.referencetemperature = convertFloat(ws.cell(row, 5).value)
                            rwMaterial.brittlefracturethickness = convertFloat(ws.cell(row, 6).value)
                            rwMaterial.allowablestress = convertFloat(ws.cell(row, 7).value)
                            rwMaterial.corrosionallowance = convertFloat(ws.cell(row, 8).value)
                            rwMaterial.carbonlowalloy = convertTF(ws.cell(row, 9).value)
                            rwMaterial.austenitic = convertTF(ws.cell(row, 10).value)
                            rwMaterial.nickelbased = convertTF(ws.cell(row, 11).value)
                            rwMaterial.chromemoreequal12 = convertTF(ws.cell(row, 12).value)
                            if ws.cell(row, 13).value:
                                rwMaterial.sulfurcontent = ws.cell(row, 13).value
                            if ws.cell(row, 14).value:
                                rwMaterial.heattreatment = ws.cell(row, 14).value
                            rwMaterial.ispta = convertTF(ws.cell(row, 15).value)
                            if ws.cell(row, 16).value:
                                rwMaterial.ptamaterialcode = ws.cell(row, 16).value
                            rwMaterial.costfactor = convertFloat(ws.cell(row, 17).value)
                            rwMaterial.save()
    except Exception as e:
        print("Exception at RwMaterial")
        print(e)

#sheet 5
def processCoating(ws):
    try:
        ncol = ws.ncols
        nrow = ws.nrows
        if ncol == 15:
            for row in range(1,nrow):
                if ws.cell(row,0).value:
                    for a in listProposal:
                        if a.componentid_id == getComponentID(ws.cell(row,0).value):
                            rwCoating = models.RwCoating.objects.get(id= a.id)
                            rwCoating.internalcoating = convertTF(ws.cell(row,1).value)
                            rwCoating.externalcoating = convertTF(ws.cell(row,2).value)
                            if ws.cell(row,3).value:
                                rwCoating.externalcoatingdate = convertDateInsp(ws.cell(row,3).value)
                            if ws.cell(row,4).value:
                                rwCoating.externalcoatingquality = ws.cell(row,4).value
                            rwCoating.supportconfignotallowcoatingmaint = convertTF(ws.cell(row,5).value)
                            rwCoating.internalcladding = convertTF(ws.cell(row,6).value)
                            rwCoating.claddingcorrosionrate = convertFloat(ws.cell(row,7).value)
                            rwCoating.internallining = convertTF(ws.cell(row,8).value)
                            if ws.cell(row,9).value:
                                rwCoating.internallinertype = ws.cell(row,9).value
                            if ws.cell(row,10).value:
                                rwCoating.internallinercondition = ws.cell(row,10).value
                            rwCoating.externalinsulation = convertTF(ws.cell(row,11).value)
                            rwCoating.insulationcontainschloride = convertTF(ws.cell(row,12).value)
                            if ws.cell(row,13).value:
                                rwCoating.externalinsulationtype = ws.cell(row,13).value
                            if ws.cell(row,14).value:
                                rwCoating.insulationcondition = ws.cell(row,14).value
                            rwCoating.save()
    except Exception as e:
        print("Exception at RwCoating")
        print(e)

def importPlanProcess(filename):
    try:
        workbook = open_workbook(filename)
        ws0 = workbook.sheet_by_name("Equipment")
        ws1 = workbook.sheet_by_name("Component")
        ws2 = workbook.sheet_by_name("Operating Condition")
        ws3 = workbook.sheet_by_name("Stream")
        ws4 = workbook.sheet_by_name("Material")
        ws5 = workbook.sheet_by_name("CoatingCladdingLiningInsulation")
        ncol0 = ws0.ncols
        ncol1 = ws1.ncols
        ncol2 = ws2.ncols
        ncol3 = ws3.ncols
        ncol4 = ws4.ncols
        ncol5 = ws5.ncols

        if (ncol0 == 32 and ncol1 == 32 and ncol2 == 18 and ncol3 == 22 and ncol4 == 22 and ncol5 == 15) or (ncol0 == 36 and ncol1 == 24 and ncol2 == 18 and ncol3 == 25 and ncol4 == 18 and ncol5 == 15):
            # step 1: processing data Equipment master
            processEquipmentMaster(ws0)
            # step 2: processing data Component master
            processComponentMaster(ws1)
            # step 3: processing data RwAssessment
            processAssessment(ws1)
            # step 4: processing data other Rw
            processRwEquipment(ws0)
            processRwComponent(ws1)
            processRwExtcor(ws2)
            processStream1(ws2)
            processStream2(ws3)
            processMaterial(ws4)
            processCoating(ws5)
    except Exception as e:
        print("Exception at import")
        print(e)
        raise Http404