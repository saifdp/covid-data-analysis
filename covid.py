# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:06:46 2022

@author: HP
"""

import pandas as pd
from matplotlib import pyplot as plt
data1=pd.read_csv("E:/codes/intern_prj_github/covid_data_analysis/coviddataset.csv")
print(data1)

n=data1.shape
print(n)

n1=n[0]
print(n1)

risk=[]

h=0
l=0

for i in range(n1):
    rec=data1.iloc[i]
    if rec[1] < 60:
        rk="low"
    else:
        rk="high"
        
    risk.append(rk)

data1["Risk Factor"]=risk
print(data1)
dt=(data1[data1=='Risk Factor'])

print(data1)

n=data1.shape
print(n)

n1=n[0]
print(n1)


for i in range(n1):
    rec=data1.iloc[i]
    if rec[10]=="high":
        h=h+1
    elif rec[10]=="low":
        l=l+1    
print(h,l)
col=["red","green"]
x=['High','Low']
y=[h,l]

plt.bar(x,y,color=col)
plt.title("Risk")
plt.xlabel("Risk Factor")
plt.ylabel("No. of Patients")
plt.show()




pos=0
neg=0

for i in range(n1):
    rec=data1.iloc[i]
    if rec[9]=="Pos":
        pos=pos+1
    elif rec[9]=="Neg":
        neg=neg+1


dcity=(data1[data1.city=="Dvg"])
dcs=dcity.shape
dcs1=dcs[0]

dpos=0
dneg=0

for i in range(dcs1):
    rec=dcity.iloc[i]
    if rec[9]=="Pos":
        dpos=dpos+1
    elif rec[9]=="Neg":
        dneg=dneg+1
        
bcity=(data1[data1.city=="Bng"])
bcs=bcity.shape
bcs1=bcs[0]

bpos=0
bneg=0

for i in range(bcs1):
    rec=bcity.iloc[i]
    if rec[9]=="Pos":
        bpos=bpos+1
    elif rec[9]=="Neg":
        bneg=bneg+1

#Gender
genp=(data1[data1.status=='Pos'])

gp=genp.shape
gp1=gp[0]

gpm=0
gpf=0

for i in range(gp1):
    rec=genp.iloc[i]
    if(rec[2]==1):
        gpm=gpm+1
    elif(rec[2]==2):
        gpf=gpf+1 
        

genn=(data1[data1.status=='Neg'])

gn=genn.shape
gn1=gn[0]

gnm=0
gnf=0

for i in range(gn1):
    rec=genn.iloc[i]
    if(rec[2]==1):
        gnm=gnm+1
    elif(rec[2]==2):
        gnf=gnf+1        

print("1.Result of all patient \n2.City wise Result")
opt=(int(input("Select Your Choice: \n")))
if opt==1:
    print("1.Positive Patients\n 2.Negative Patient: \n")
    opt1 = int(input("Search all patient covid result:\n "))
    
    if opt1==1:
        print(data1[data1.status=="Pos"])
        print("All Positive Patients :",pos)
        print("1.Male\n2.Female")
        optt=int(input("Enter Gender: "))
        if optt==1:
            print("No. of Male Positive patients: ",gpm)
        elif optt==2:
            print("No. of Female Positive patients: ",gpf)    
        
    elif opt1==2:
        print(data1[data1.status=="Neg"])
        print("Negative Patients :",neg)
        print("1.Male\n2.Female")
        optt=int(input("Enter Gender: "))
        if optt==1:
            print("No. of Male Negative patients: ",gnm)
        elif optt==2:
            print("No. of Female Negative patients: ",gnf)
    
elif opt==2:
    print("City wise results")
    print("1.Dvg\n2.Bng")
    opt2=int(input("Select city: \n"))
    if opt2==1:
        print(data1[data1.city=="Dvg"])
        print("Dvg positive patients: ",dpos)
        print("Dvg negative patients: ",dneg)
        x=["Positve","Negative"]
        y=[dpos,dneg]
        plt.title("Davangere COVID Result")
        plt.pie(y,labels=x,autopct="%0.1f%%")
        plt.legend()
        plt.show()
    elif opt2==2:
        print(data1[data1.city=="Bng"])
        print("Bng positive patients: ",bpos)
        print("Bng negative patients: ",bneg)
        x=["Positve","Negative"]
        y=[bpos,bneg]
        plt.title("Bangalore COVID Result")
        plt.pie(y,labels=x, autopct="%0.1f%%")
        plt.legend()
        plt.show()

    
        