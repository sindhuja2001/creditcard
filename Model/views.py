from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import joblib
import numpy as np
import webbrowser
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .models import (Userlogin, ManualInput)
from django.core import serializers
from django.shortcuts import redirect,reverse
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
def home(request):
    print("home...................")
    return render(request,"index.html")
    
def loginpage(request):
    print("login......................")
    return render(request, "login.html")

def newAccount(request):
    print("aaaaaaaaaaaaaaaaaaaaaaaa")
    return render(request,"newAccount.html")

def report(request):
    print("report...")
    return render(request, "result.html")

# def report(request):
#     print("arunanibi")
#     return render(request,"result.html")

# def finaloutput(request):
#      template = loader.get_template('result.html')
#      context = {
#         'result':prediction    
#   }
#     return HttpResponse(template.render(context, request))

# def result(request):
#     print("result..................")
#     cls = joblib.load('CreditCardFraudDetection.joblib')
   
#     loginName = request.GET['year']
#     loginName =removeGaps(loginName)
#     l = []
#     s=""
#     for x in loginName:
#         if x in[" ",",","	","    "]:
#             l.append(float(s))
#             s=""
#         else:
#             s+=x
#     l.append(float(s))     

#     features = [np.array(l)]
#     prediction = cls.predict(features)
#     if prediction == 0:
#         prediction= "Non-Fraudulent Transaction"
#     else:
#         prediction= "Fraudulent Transaction"
#     return render("index.html", prediction_text = "Predicted output is :     {}".format(prediction))
#     return JsonResponse({"result":prediction})
#     return render(request, 'index.html', {'prediction': prediction})


class result(CreateAPIView):
    permission_classes = (AllowAny,)
    print("result..................")
    def create(self, request, *args, 
    **kwargs):
        # cls = joblib.load('CreditCardFraudDetection.joblib')
    
        # loginName = request.data['data']['data']
        try:
            id = request.data['data']['datas']['id']
        except:
            id = None
        # print(request.data['data']['Time']+"Aruna")
       
        time = request.data['data']['datas']['Time']
        v1 = request.data['data']['datas']['V1']
        v2 = request.data['data']['datas']['V2']
        v3 = request.data['data']['datas']['V3']
        v4 = request.data['data']['datas']['V4']
        v5 = request.data['data']['datas']['V5']
        v6 = request.data['data']['datas']['V6']
        v7 = request.data['data']['datas']['V7']
        v8 = request.data['data']['datas']['V8']
        v9 = request.data['data']['datas']['V9']
        v10 = request.data['data']['datas']['V10']
        v11 = request.data['data']['datas']['V11']
        v12 = request.data['data']['datas']['V12']
        v13 = request.data['data']['datas']['V13']
        v14 = request.data['data']['datas']['V14']
        v15 = request.data['data']['datas']['V15']
        v16 = request.data['data']['datas']['V16']
        v17 = request.data['data']['datas']['V17']
        v18 = request.data['data']['datas']['V18']
        v19 = request.data['data']['datas']['V19']
        v20 = request.data['data']['datas']['V20']
        v21 = request.data['data']['datas']['V21']
        v22 = request.data['data']['datas']['V22']
        v23 = request.data['data']['datas']['V23']
        v24 = request.data['data']['datas']['V24']
        v25 = request.data['data']['datas']['V25']
        v26 = request.data['data']['datas']['V26']
        v27 = request.data['data']['datas']['V27']
        v28 = request.data['data']['datas']['V28']
        amount = request.data['data']['datas']['Amount']
        if not id:
            ManualInput.objects.create(
                Time = time,
                V1 = v1,
                V2 = v2,
                V3 = v3,
                V4 = v4,
                V5 = v5,
                V6 = v6,
                V7 = v7,
                V8 = v8,
                V9 = v9,
                V10 = v10,
                V11 = v11,
                V13 = v13,
                V12 = v12,
                V14 = v14,
                V15 = v15,
                V16 = v16,
                V17 = v17,
                V18 = v18,
                V19 = v19,
                V20 = v20,
                V21 = v21,
                V22 = v22,
                V23 = v23,
                V24 = v24,
                V25 = v25,
                V26 = v26,
                V27 = v27,
                V28 = v28,
                Amount =amount
            )
        else:
            print("elsepart")
            manualinput = ManualInput.objects.get(pk = id)
            manualinput.Time = time
            manualinput.V1 = v1
            manualinput.V2 = v2
            manualinput.V3 = v3
            manualinput.V4 = v4
            manualinput.V5 = v5
            manualinput.V6 = v6
            manualinput.V7 = v7
            manualinput.V8 = v8
            manualinput.V9 = v9
            manualinput.V10 = v10
            manualinput.V11 = v11
            manualinput.V12 = v12
            manualinput.V13 = v13
            manualinput.V14 = v14
            manualinput.V15 = v15
            manualinput.V16 = v16
            manualinput.V17 = v17
            manualinput.V18 = v18
            manualinput.V19 = v19
            manualinput.V20 = v20
            manualinput.V21 = v21
            manualinput.V22 = v22
            manualinput.V23 = v23
            manualinput.V24 = v24
            manualinput.V25 = v25
            manualinput.V26 = v26
            manualinput.V27 = v27
            manualinput.V28 = v28
            manualinput.Amount = amount

            manualinput.save()           
        return JsonResponse({"success":True})

class predicte(CreateAPIView):
    permission_classes = (AllowAny,)
    print("entered..................")
    def create(self, request, *args, **kwargs):
        loginName = request.data['data']['entire_data']
        print(loginName)
        cls = joblib.load('CreditCardFraudDetection.joblib')
        
        value = loginName.split(",")
        print(value)
        values = []
        for v in value:
            float_val=float(v) 
            print(type(float_val))          
            values.append(float_val)
        print(values)
        features = [np.array(values)]
        prediction = cls.predict(features)
        if prediction == 0:
            prediction= "Non Fraudulent Transaction"
        else:
            prediction= "Fraudulent Transaction"

        print({'result':prediction})
        # template = loader.get_template('result.html')
        context = {
           'result':prediction,
           'value':values
        }
        # print(context)
        # return render(request,"index.html",{'result':prediction})
        # return HttpResponseRedirect("/result.html/")
        # return HttpResponse(template.render(context, request))
        # redirect("report/")
        # c = webbrowser.get('chrome')
        # url = http://127.0.0.1:8000/report/?result=" . $&values"=$loginName
        webbrowser.open('http://127.0.0.1:8000/report/?result='+ prediction, new=0)
        
        return JsonResponse({'result' : prediction})
        # return JsonResponse(context)

             
# def removeGaps(loginName):
#         h =""
#         for v in loginName:
#             if v in['1','2','3','4','5','6','7','8','9','0','-','.',',']:
#                 h+=v

#         return h

class authenticat(CreateAPIView):
    permission_classes = (AllowAny,)
    users = Userlogin.objects.all()
    print("XXXXXXXXXXx",users)
    # def get(self, request):
    def create(self, request, *args, **kwargs):
        print("glooo",request.data)
        email = request.data['data']['email']
        password = request.data['data']['password']
        print(email)
        print(password)

        users = Userlogin.objects.all()
        print(users)
        for x in users:
            print(x.email==email)
            print(x.mailPassword==password)
            if x.email == email and x.mailPassword == password:
                print("YYYYYYYYYYYYYYYYY")
                return JsonResponse({"success":True})

        return JsonResponse({"success":False})


 

class addUser(CreateAPIView):
    permission_classes = (AllowAny,)
    print("YYYYYYYYYYYYYYYYYY")
    # def get(self, request):
    def create(self, request, *args, **kwargs):
        print("glooo",request.data)
        email = request.data['data']['email']
        password = request.data['data']['password']
        print(email)
        print(password)
        users = Userlogin.objects.all()
        for x in users:
            if x.email ==email:
                print("AAAAAAAAAAAAAAAAAAAAa")
                return JsonResponse({"success":False})
        Userlogin.objects.create(
            email = email,
            mailPassword = password
        )
        return JsonResponse({"success":True})