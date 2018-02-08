"""rbi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from  django.contrib import admin
from  home import views

urlpatterns = [
    # Project Management URL
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^contact/$', views.contact, name='contact'),

    # RBI 581 INFO URL
    # New URL
    url(r'^site/new/$', views.newSite, name='newSite'),
    url(r'^site/(?P<siteid>\d+)/facility/new/$', views.facility, name='facility'),
    url(r'^facility/(?P<facilityname>\d+)/equipment/new/$', views.equipment, name='equipment'),
    url(r'^equipment/(?P<equipmentname>\d+)/component/new/$', views.newcomponent, name='component'),
    url(r'^facility/(?P<facilityname>\d+)/designcode/new/$', views.newDesigncode, name='newdesigncode'),
    url(r'^facility/(?P<facilityname>\d+)/manufacture/new/$', views.newManufacture, name='newmanufacture'),
    url(r'^component/(?P<componentname>\d+)/proposal/new/$', views.newProposal , name='newProposal'),
    url(r'^component/(?P<componentname>\d+)/tank/proposal/new/$', views.newProposalTank, name='newProposalTank'),
    # Edit URL
    url(r'^site/(?P<sitename>\w+)/edit/$', views.editSite, name='editsite'),
    url(r'^site/(?P<sitename>\d+)/facility/(?P<facilityname>\d+)/edit/$', views.editFacility, name='editfacility'),
    url(r'^facility/(?P<facilityname>\d+)/equipment/(?P<equipmentname>\d+)/edit/$', views.editEquipment, name='editequipment'),
    url(r'^facility/(?P<facilityname>\d+)/designcode/(?P<designcodeid>\d+)/edit/$', views.editDesignCode, name='editdesigncode'),
    url(r'^facility/(?P<facilityname>\d+)/manufacture/(?P<manufactureid>\d+)/edit/$', views.editManufacture, name='editmanufacture'),
    url(r'^equipment/(?P<equipmentname>\d+)/component/(?P<componentname>\d+)/edit/$', views.editComponent, name='editcomponent'),
    # Display URL
    url(r'^site/display/$', views.site_display, name='site_display'),
    url(r'^facility/(?P<facilityname>\d+)/equipment/display/$', views.equipmentDisplay, name='equipment_display'),
    url(r'^equipment/(?P<equipmentname>\d+)/component/display/$', views.componentDisplay, name='component_display'),
    url(r'^site/(?P<sitename>\d+)/facility/display/$', views.facilityDisplay, name='facilityDisplay'),
    url(r'^facility/(?P<facilityname>\d+)/designcode/$', views.designcodeDisplay, name='designcodeDisplay'),
    url(r'^facility/(?P<facilityname>\d+)/manufacture/$', views.manufactureDisplay, name='manufactureDisplay'),
    url(r'^proposal/(?P<proposalname>\d+)/result/CA/$', views.displayCA, name='resultca'),
    url(r'^proposal/(?P<proposalname>\d+)/result/DF/$', views.displayDF, name='resultdf'),
    url(r'^proposal/(?P<proposalname>\d+)/result/POF/$', views.displayFullDF, name='resultpof'),
    url(r'^component/(?P<componentname>\d+)/proposal/display/$', views.displayProposal, name= 'proposalDisplay'),
    # Proposal URL( RBI 581 calculate URL)

]
