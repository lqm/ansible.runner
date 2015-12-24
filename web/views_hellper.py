#!/usr/bin/env python
#coding:utf-8
from web.models import Asset,UserInfo,machine_list,group_fuckid


def str_change(obj_list):
    temp3 = []
    for temp in obj_list:
        temp1 = list(temp)
        temp2 = temp1[0].encode("utf8")
        temp3.append(temp2)
       # print temp3
    obj_list = temp3
    
    return obj_list

def userbygroup():
    obj_list = machine_list.objects.values_list('Use_by_group')
    obj_list = obj_list.distinct()
    
    
    obj_list = str_change(obj_list)
    obj_list.pop(0)
    ret = {'obj_list': obj_list}
  
    return ret
def sqlselect_front(a):
    obj_list = machine_list.objects.values_list(a)
    obj_list = obj_list.distinct()
    
    
    obj_list = str_change(obj_list)
   # obj_list.pop(0)
    ret = {a: obj_list}
  
    return ret

def sqlselect_getValue(key,value):
    obj_list = machine_list.objects.get(key=value)
    return obj_list   


def group_fuckid_getValue(a):
    obj_list = group_fuckid.objects.values_list(a)
    obj_list = obj_list.distinct()
    
    
    obj_list = str_change(obj_list)
   # obj_list.pop(0)
    ret = {a: obj_list}
  
    return ret