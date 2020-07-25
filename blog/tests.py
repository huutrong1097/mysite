# from django.test import TestCase

# Create your tests here.

# lists=[1,2,3,4,5,2,3]
# for i in range(len(lists)): 
#     k = i + 1
#     for j in range(k, len(lists)): 
#         if lists[i] == lists[j]:
#             print(True)
from netaddr import *
list_ips=[]
subnet='172.29.73.240/28'
for ips in IPNetwork(subnet):
    print(ips)
    list_ips.append('%s' % ips)
# ip = IPNetwork('27')
# print(ip.netmask)