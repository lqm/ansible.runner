#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
os.environ['DJANGO_SETTINGS_MODULE']='yunwei_plant.settings'
import sys

#user=sys.argv[1]
#passwd=sys.argv[2]
#userselect=sys.arg[1]


#userselect='node'
user='lqm'
passwd='liuqimin@123'


from web.models_sql import ansible_host_getall
result = ansible_host_getall()
jump_group_ip={}
ip=[]
for group,ip in result:
   # print ip_address[0]
    #print ip
    #print group
    if jump_group_ip.has_key(group):
       ip=str(ip)
      # list[jump_group_ip[group]].append(ip)
      # jump_group_ip[group].append(ip)
    else:
       ip=str(ip)
       group=str(group)
       #print ip
       jump_group_ip[group]=dict()
       jump_group_ip[group]["hosts"]=list()
      # print jump_group_ip[group]
      # list[jump_group_ip[group]]=[ip]
    jump_group_ip[group]["hosts"].append(ip)
    # list[jump_group_ip[group]].append(ip)
    #ip.append(ip_address[0])
print json.dumps(jump_group_ip)
