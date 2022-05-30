import email
from urllib import response
from django.shortcuts import render
from numpy import roll

from .models import *


def home(request):
    return render(request,"home.html")



def data(request):
    #  first = request.POST["fname"]
     num1 = request.POST["fname"]
     num2 = request.POST["lname"]
     data = TEMP(first_name = num1 , last_name = num2 )
     data.save() 
     
     return render(request,"home.html")
 
     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",data.first_name)
     return render(request,"data.html",{"fname":data.first_name})


def display_Mydata(request):
    #  first = request.POST["fname"]
    
    
    #  num1 = request.POST["fname"]
    #  num2 = request.POST["lname"]
    #  data = TEMP(first_name = num1 , last_name = num2 )
    #  data.save() 
     
     mydata = TEMP.objects.all()
     
     for x in mydata:
         print(x.first_name,">>>>>>>>",x.last_name,"\n\n")
     return render(request,"data.html",{"fname":mydata})
 
 
 
def registration12(request):
    return render(request,"login.html")



    
    
def registration_data(request):
    first_name = request.POST["fname"]
    last_name = request.POST["lname"]
    dep_name = request.POST["department"]
    roll_no = request.POST["rollno"]
    address = request.POST["address"]
    gender = request.POST["gender"]
    dob = request.POST["dob"]
    pincode = request.POST["pincode"]
    resume = request.POST["resume"]
    email_id = request.POST["email"]
    password = request.POST["password"]

    
    print("first name: ",first_name,"\nlast name: ",last_name,"\ndep name: ",dep_name,"\nroll : ",roll_no,"\nnaddress: ",address,"\ngender: ",gender,"\ndob",dob,"\npin: ",pincode,"\nresume: ",resume,"\nemail: ",email_id)
    
    Mydata = registration1(first_name = first_name, last_name = last_name,dep_name = dep_name, roll_no = roll_no, address = address, gender = gender, dob = dob, pincode = pincode, resume = resume, email_id = email_id, password = password)
    Mydata.save() 
    
    return render(request,"data.html")
 
 
 
def std_login(request):
    return render(request,"stdlogin.html")


def student_logged_in(request):
    
    email_id = request.POST["email"]
    password = request.POST["password"]
    
    logn = registration1.objects.all()
    for d in logn:
        if email_id == d.email_id and password == d.password:
            print("yes")
            
            return render(request,"data.html",{"fname": d.first_name,"lname":d.last_name})
        
    return render(request,"stdlogin.html")
            
    #     print("emial : ",d.email_id)
    #     print("\npassword : ",d.password)
    #     print("\n____________________________\n")
    # print(">>>>>>>>>>>>>>>>>>>>>>>>><<<>>",email_id,password)
    # return render(request,"data.html",{"email_id": email_id,"password":password})
 
 
def company(request):
    return render(request,"company.html")
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#  from django.shortcuts import render


# from .models import mydata




# def home(request):
    
#     data = mydata()
#     data.name = "harsha"
#     data.phone_no = 123456789
#     data.extra = "Test 1"

#     data1 = mydata()
#     data1.name = "jack"
#     data1.phone_no = 98765432
#     data1.extra = "Test 2"
    
#     data2 = mydata()
#     data2.name = "aman"
#     data2.phone_no = 123
#     data2.extra = "Test 3"
    
    
#     file = [data, data1, data2]
    
#     return render(request,"home.html",{"key":file})