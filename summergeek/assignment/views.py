from django.shortcuts import render
import time
import datetime
from django.core.mail import send_mail
from django.conf import settings
import zerosms #it is way2sms which is used to send sms
# Create your views here.

def index(request):
    return render(request,"index.html")

def sendMailHost(Details,emailTo):
    r=send_mail('NewVisitor',
		 Details, 
		 settings.EMAIL_HOST_USER,
		 [emailTo], 
		 fail_silently=False)
    return r

def result(request):
    #if that checkout time is reached automatically send email
    if request.method=="POST":
        visitorName = request.POST.get('visitorName', '')
        visitorEmail = request.POST.get('visitorEmail', '')
        visitorPhone = request.POST.get('visitorPhone', '')
        visitorCheckIn = request.POST.get('visitorCheckIn')
        visitorCheckOut = request.POST.get('visitorCheckOut')
        hostName = request.POST.get('hostName', '')
        hostEmail = request.POST.get("hostEmail","")
        hostPhone = request.POST.get("hostPhone","")
    
    

    #print(visitorCheckIn,visitorCheckOut)
    Details=f"Name:{visitorName}\n Email:{visitorEmail}\n Phone:{visitorPhone}\n CheckIn:{visitorCheckIn}\n CheckOut:{visitorCheckOut}"
    r=sendMailHost(Details,hostEmail)
    sendSMSHost(Details,hostPhone)
    #sending visitor email upon checkout
    sendSMSVisitor(Details,visitorPhone)
    sendMailVisitor(Details,visitorCheckOut,visitorEmail)

    #return render(request,'response.html',{"r":r})
    #sending host an email


def sendSMSHost(Details,hostPhone):
    #here we need to have an account on zerosms to send 
    #credentials of the account required
    #phone number
    #password
    zerosms.sms(phno=phonenum,passwd=password,message=Details,receivernum=hostPhone)


def sendSMSVisitor(Details,visitorPhone):
    #here we need to have an account on zerosms to send 
    #credentials of the account required
    #phone number
    #password
    zerosms.sms(phno=phonenum,passwd=password,set_time=visitorCheckOut,set_date=datetime.date.today(),message=Details,receivernum=visitorPhone)

def sendMailVisitor(Details,visitorCheckOut,visitorEmail):
    unix=int(time.time())
    ti=str(datetime.datetime.fromtimestamp(unix).strftime("%I:%M:%S:%p"))
    ti=ti.split(":")
    if ti[-1]=='PM':
        hr=ti[0]
        hr=int(hr)
        hr+=12
    else:
        hr=ti[0]
    nti=':'.join[f'{hr}',ti[1]]
    notSent=True
    while notSent:
        if nti==visitorCheckOut:
            send_mail('NewVisitor',Details, settings.EMAIL_HOST_USER,[visitorEmail], fail_silently=False)
            notSent=False

