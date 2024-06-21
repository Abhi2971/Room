# 1 may to 30 may

R_rent=8000
l_bill=2900
G_bill=0
may_dict={
    "Abhi":0,
    "Ganesh":0,
    "Hemant":0,
    "Sunil":0,
    "kiran":0,
    "KB":0
}
for key,value in may_dict.items():
    may_dict[key]=R_rent/len(may_dict)+l_bill/len(may_dict)+G_bill/len(may_dict)
print(may_dict)