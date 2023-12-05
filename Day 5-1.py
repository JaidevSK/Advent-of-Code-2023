# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:56:29 2023

@author: jaidev
"""


file1 = open('seeds_soil.txt', 'r')
Lines = file1.readlines()
seed_soilD={}
ssd=[]
sss=[]
ssr=[]
for line in Lines:
    a=line.strip()
    ssd.append(int(a.split(" ")[0]))
    sss.append(int(a.split(" ")[1]))
    ssr.append(int(a.split(" ")[2]))
for i in range(len(sss)):
    for j in range(ssr[i]):
        seed_soilD[sss[i]+j]=ssd[i]+j
        


file2 = open('soil_fert.txt', 'r')
Lines = file2.readlines()
soil_fertD={}
sfd=[]
sfs=[]
sfr=[]
for line in Lines:
    a=line.strip()
    sfd.append(int(a.split(" ")[0]))
    sfs.append(int(a.split(" ")[1]))
    sfr.append(int(a.split(" ")[2]))
for i in range(len(sfs)):
    for j in range(sfr[i]):
        soil_fertD[sfs[i]+j]=sfd[i]+j
        


file3 = open('fert_water.txt', 'r')
Lines = file3.readlines()
fert_waterD={}
fwd=[]
fws=[]
fwr=[]
for line in Lines:
    a=line.strip()
    fwd.append(int(a.split(" ")[0]))
    fws.append(int(a.split(" ")[1]))
    fwr.append(int(a.split(" ")[2]))
for i in range(len(fws)):
    for j in range(fwr[i]):
        fert_waterD[fws[i]+j]=fwd[i]+j
        
        
        
file4 = open('water_light.txt', 'r')
Lines = file4.readlines()
water_lightD={}
wld=[]
wls=[]
wlr=[]
for line in Lines:
    a=line.strip()
    wld.append(int(a.split(" ")[0]))
    wls.append(int(a.split(" ")[1]))
    wlr.append(int(a.split(" ")[2]))
for i in range(len(wls)):
    for j in range(wlr[i]):
        water_lightD[wls[i]+j]=wld[i]+j


file5 = open('light_temp.txt', 'r')
Lines = file5.readlines()
light_tempD={}
ltd=[]
lts=[]
ltr=[]
for line in Lines:
    a=line.strip()
    ltd.append(int(a.split(" ")[0]))
    lts.append(int(a.split(" ")[1]))
    ltr.append(int(a.split(" ")[2]))
for i in range(len(lts)):
    for j in range(ltr[i]):
        light_tempD[lts[i]+j]=ltd[i]+j
        
    

file6 = open('temp_humid.txt', 'r')
Lines = file6.readlines()
temp_humidD={}
thd=[]
ths=[]
thr=[]
for line in Lines:
    a=line.strip()
    thd.append(int(a.split(" ")[0]))
    ths.append(int(a.split(" ")[1]))
    thr.append(int(a.split(" ")[2]))
for i in range(len(ths)):
    for j in range(thr[i]):
        temp_humidD[ths[i]+j]=thd[i]+j



file7 = open('humid_loc.txt', 'r')
Lines = file7.readlines()
humid_locD={}
hld=[]
hls=[]
hlr=[]
for line in Lines:
    a=line.strip()
    hld.append(int(a.split(" ")[0]))
    hls.append(int(a.split(" ")[1]))
    hlr.append(int(a.split(" ")[2]))
for i in range(len(hls)):
    for j in range(hlr[i]):
        humid_locD[hls[i]+j]=hld[i]+j


file8 = open('seeds.txt', 'r')
Lines = file8.readlines()
for line in Lines:
    seeds_lis=line.strip().split(" ")
    seeds_lis = list(map(int, seeds_lis))
    
loc_lis=[]

for seed in seeds_lis:
    if seed in seed_soilD.keys():
        soil=seed_soilD[seed]
    else:
        soil=seed
    if soil in soil_fertD.keys():
        fert=soil_fertD[soil]
    else:
        fert=soil
    if fert in fert_waterD.keys():
        water=fert_waterD[fert]
    else:
        water=fert
    if water in water_lightD.keys():
        light=water_lightD[water]
    else:
        light=water
    if light in light_tempD.keys():
        temp=light_tempD[light]
    else:
        temp=light
    if temp in temp_humidD.keys():
        humid=temp_humidD[temp]
    else:
        humid=temp
    if humid in humid_locD.keys():
        loc=humid_locD[humid]
    else:
        loc=humid
    loc_lis.append(loc)

print(min(loc_lis))
    