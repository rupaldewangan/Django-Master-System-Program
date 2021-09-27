# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:02:30 2019

@author: RUPAL
"""

from django.shortcuts import render
import csv
import mysql.connector as sqltor

def home(request):
    return render(request,'home.html')

def frontdata(request):
    return render(request,'forntdata.html')

def frontpage(request):
    ssclna = request.GET.get('Psclnam','default')
    sroll = request.GET.get('PRolln','default')
    ssess = request.GET.get('Psess','default')
    sfirst = request.GET.get('PFirste','default')
    ssub = request.GET.get('Psub','default')
    spst = request.GET.get('Pst','default')
    sclass = request.GET.get('PCLASS','default')
    stopic = request.GET.get('PTOPIC','default')
    stechdeg = request.GET.get('PTECHDEG','default')
    surl = request.GET.get('PURL','default')
    pag = {'psc':ssclna,'srl':sroll,'ssee':ssess,
           'sfrn':sfirst,'ssb':ssub,'sts':spst,
           'sscl':sclass,'stp':stopic,'stechd':stechdeg,
           'srllll':surl}
    RD2 = [ssclna,sroll,ssess,sfirst,ssub,spst,sclass,stopic,stechdeg,surl]
    with open('Front Page Data .csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(RD2)
    csvFile.close()
    return render(request,'frontpage.html',pag)
def ackdata(request):
    return render(request,'ackadata.html')
def acknowledgement(request):
    psclna = request.GET.get('rsclnam','default')
    pprinci = request.GET.get('rprincipal','default')
    psubt = request.GET.get('rsubtec','default')
    pfir = request.GET.get('rFirste','default')
    psb = request.GET.get('rsub','default')
    pstdg = request.GET.get('rstg','default')
    
    para = {'pscl':psclna,'pp':pprinci,'psuteh':psubt,
            'ppre':pfir,'psubt':psb,'pdeg':pstdg }
    RD1 =[psclna,pprinci,psubt,pfir,psb,pstdg]
    with open('Acknowledgemnt Data .csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(RD1)
    csvFile.close()
    return render(request,'acknowledgement.html',para)
def iddata(request):
    return render(request,'idata.html')
def ido(request):
    isclna = request.GET.get('sclnameee','default')
    isadd = request.GET.get('adresss','default')
    isclcon = request.GET.get('cont','default')
    istudentname = request.GET.get('Firsterrr','default')
    isphone = request.GET.get('sphonee','default')
    istuadd = request.GET.get('Saddd','default')
    isturl = request.GET.get('ssurl','default')
    isclurl = request.GET.get('sturl','default')
    
    parame = {'sclname':isclna,'isaddd':isadd,'isclconnn':isclcon,'istuden':istudentname,
              'istuph':isphone,'iadd':istuadd,'iurl':isturl,'isclurl':isclurl}
    rd =[isclna,isadd,isclcon,istudentname,isphone,istuadd,isturl,isclurl]
    with open('ID Card.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(rd)
    csvFile.close()
    
    return render (request,'ido.html',parame)
def certidata(request):
    return render(request,'certiget.html')

def certificate(request):
    sclna = request.GET.get('sclnam','default')
    rol = request.GET.get('Rolln','default')
    sessi = request.GET.get('sess','default')
    frnm = request.GET.get('Firste','default')
    sube = request.GET.get('sub','default')
    subt = request.GET.get('st','default')
    s=str(sclna)
    r=str(rol)
    se=str(sessi)
    f=str(frnm)
    su=str(sube)
    sub=str(subt)
    
    exe1=[sclna,rol,sessi,frnm,sube,subt]
    with open('CERTIFICATE DATA.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(exe1)
    csvFile.close()
    mycon = sqltor.connect(host="localhost",user="root",passwd="rupal",database='website')
    if mycon.is_connected():
        print("sucesss")
    cursor=mycon.cursor()
    cdata="insert into certificatedata values('{}','{}','{}','{}','{}','{}')".format(s,r,se,f,su,sub)
    cursor.execute(cdata)
    mycon.commit()
    
    param = {'sn':sclna,'rln':rol,'sessssion':sessi,
             'firname':frnm,'subee':sube,'subec':subt}
    return render(request,'certificate.html',param)

def index(request):
    return render(request,'index.html')
    
def result(request):
    sclname = request.GET.get('sclname','default')
    rollno = request.GET.get('Rollno','default')
    firstname = request.GET.get('Firstname','default')
    doob = request.GET.get('dob','default')
    gender = request.GET.get('gn','default')
    cse = request.GET.get('cs','default')
    math = request.GET.get('math','default')
    phy = request.GET.get('phy','default')
    chem = request.GET.get('chem','default')
    eng = request.GET.get('eng','default')
    phe = request.GET.get('pe','default')
    fatna = request.GET.get('fn','default')
    matnam = request.GET.get('mn','default')
    clss = request.GET.get('clsas','default')
    session = request.GET.get('ses','default')
    section = request.GET.get('sec','default ')
    totalatt = request.GET.get('tat','default')
    netatt = request.GET.get('net','default')
   
    OM = int(cse)+int(math)+int(phy)+int(chem)+int(eng)+int(phe)
    ase=str(OM)
    e=int(eng)    
    if e>90 and e<=100:
        gradee='A+'
    elif e>80 and e<=90:
        gradee='A'
    elif e>70 and e<=80:
        gradee='B+'
    elif e>60 and e<=70:
        gradee='B'
    elif e>50 and e<=60:
        gradee='C+'
    elif e>33 and e<=50:
        gradee='C'
    elif e>0 and e<=33:
        gradee='D'
    else:
        gradee("Number are not inputed correctly")
    ph=int(phe)    
    if ph>90 and ph<=100:
        gradeph='A+'
    elif ph>80 and ph<=90:
        gradeph='A'
    elif ph>70 and ph<=80:
        gradeph='B+'
    elif ph>60 and ph<=70:
        gradeph='B'
    elif ph>50 and ph<=60:
        gradeph='C+'
    elif ph>33 and ph<=50:
        gradeph='C'
    elif ph>0 and ph<=33:
        gradeph='D'
    else:
        gradeph("Number are not inputed correctly")
    ch=int(chem)
    if ch>90 and ch<=100:
        gradech='A+'
    elif ch>80 and ch<=90:
        gradech='A'
    elif ch>70 and ch<=80:
        gradech='B+'
    elif ch>60 and ch<=70:
        gradech='B'
    elif ch>50 and ch<=60:
        gradech='C+'
    elif ch>33 and ch<=50:
        gradech='C'
    elif ch>0 and ch<=33:
        gradech='D'
    else:
        gradech("Number are not inputed correctly")
        
    p=int(phy)    
    if p>90 and p<=100:
        gradep='A+'
    elif p>80 and p<=90:
        gradep='A'
    elif p>70 and p<=80:
        gradep='B+'
    elif p>60 and p<=70:
        gradep='B'
    elif p>50 and p<=60:
        gradep='C+'
    elif p>33 and p<=50:
        gradep='C'
    elif p>0 and p<=33:
        gradep='D'
    else:
        gradep("Number are not inputed correctly")
        
    m=int(math)
    if m>90 and m<=100:
        gradem='A+'
    elif m>80 and m<=90:
        gradem='A'
    elif m>70 and m<=80:
        gradem='B+'
    elif m>60 and m<=70:
        gradem='B'
    elif m>50 and m<=60:
        gradem='C+'
    elif m>33 and m<=50:
        gradem='C'
    elif m>0 and m<=33:
        gradem='D'
    else:
        gradem("Number are not inputed correctly")
        
        
    c=int(cse)
    if c>90 and c<=100:
        gradec='A+'
    elif c>80 and c<=90:
        gradec='A'
    elif c>70 and c<=80:
        gradec='B+'
    elif c>60 and c<=70:
        gradec='B'
    elif c>50 and c<=60:
        gradec='C+'
    elif c>33 and c<=50:
        gradec='C'
    elif c>0 and c<=33:
        gradec='D'
    else:
        gradec("Number are not inputed correctly")
        
    OP = (OM/600)*100
    asp=str(OP)+"%"
    if OP>90 and OP<=100:
        grade='A+'
    elif OP>80 and OP<=90:
        grade='A'
    elif OP>70 and OP<=80:
        grade='B+'
    elif OP>60 and OP<=70:
        grade='B'
    elif OP>50 and OP<=60:
        grade='C+'
    elif OP>33 and OP<=50:
        grade='C'
    elif OP>0 and OP<=33:
        grade='D'
    else:
        grade("Number are not inputed correctly")
    if OP>33 and OP<=100:
        resulttt='PASS'
    elif OP>0 and OP<=33:
        resulttt='FAILED'
    else:
        resulttt='Check the filled data and Summit it again'
    
    
    exe=[sclname,rollno,firstname,doob,gender,cse,math,phy,chem,eng,phe,fatna,matnam,clss,session,
         section,totalatt,netatt,ase,asp,resulttt]
    
    with open('Student Data and Result.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(exe)
    csvFile.close()
    para ={'scl':sclname,'rn':rollno,'firn':firstname,'dog':doob,
           'gen':gender,
           
           'com':cse,'mat':math,'physi':phy,
           'chemis': chem, 'engli':eng,'physical':phe,
           
           'grdc':gradec,'grdm':gradem,'grdp':gradep,
           'grdch':gradech,'grdph':gradeph,'grde':gradee,
           
           'fatname':fatna,'mother':matnam,'claass':clss,
           'sessions':session,
           
           'sect':section,'totatt':totalatt,
           'netatt':netatt,
           'om':OM,'op':OP,'grd':grade,'ress':resulttt}
    return render(request,'res.html',para)

def about(request):
    return render(request,'abt.html')

def contact(request):
    return render(request,'conc.html')
    

                       
