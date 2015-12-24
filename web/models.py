#!/usr/bin/env python
#coding:utf-8
from django.db import models

from django.db.models.fields.related import OneToOneField
from MySQLdb.constants.FLAG import UNIQUE
# Create your models here.
   
class UserType(models.Model): 
    name = models.CharField(max_length=50)  
    
class UserInfo(models.Model):
    
    username = models.CharField(max_length=50)
    
    password = models.CharField(max_length=50)
    
  
    
  
    
    memo = models.TextField(default = 'xxxx')
    
    CreateDate = models.DateTimeField(default='2014-12-12 12:12')
    
 
 


class Group(models.Model):
    
    Name = models.CharField(max_length=50)
    
    
class User(models.Model):
    Name = models.CharField(max_length=50)
    
    Email = models.CharField(max_length=50)
    
    group_relation = models.ManyToManyField('Group')
    #OneToOneField
    
class Args(models.Model):
    
    name = models.CharField(max_length=20,null=True)
    
    not_name = models.CharField(max_length=20,null=False)
    



class Asset(models.Model):
    
    hostname  = models.CharField(max_length=256)
    
    create_date = models.DateTimeField(auto_now_add = True)
    
    update_date = models.DateTimeField(auto_now=True,error_messages={"invalid":'日期格式错误'})  




class UserInfo_Temp(models.Model):
    
    #用户名，密码、Email
    
    GENDER_CHOICE = (
        (u'1', u'普通用户'),
        (u'2', u'管理员'),
        (u'3', u'超级管理员'),
        )
    UserType = models.CharField(max_length=2,choices = GENDER_CHOICE)
    
class machine_list(models.Model):
    #服务器清单存放
    
    hostname = models.CharField(max_length=256)
    
    ip_address = models.IPAddressField(unique=True)
    
    Use_by_group = models.CharField(max_length=30)
    
    group_list = models.CharField(max_length=256)
    
    
    contact_dev = models.IPAddressField()

    
    
class group_fuckid(models.Model):
    
    Use_by_group = models.CharField(max_length=30,primary_key=True)
    unic_group = models.CharField(max_length=50,unique=True)
    
    def __unicode__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.Use_by_group
    
class ansible_hosts(models.Model):
    #服务器清单存放
    
    ip_address = models.IPAddressField()
    
    unic_group = models.CharField(max_length=50,unique=True)
    


        

