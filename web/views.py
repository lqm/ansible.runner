#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.http.response import HttpResponse
from web.models import Asset,UserInfo,machine_list,group_fuckid
from django.template.context import RequestContext
from django.utils.safestring import mark_safe
from web import common
from web import views_hellper
from web import html_helper,models_sql
#from django.db import models,connection
from django import forms
import ansible.runner
import ansible.inventory
import os,re,commands 
try:
    import json
except ImportError:
    import simplejson as json


#class AddForm(forms.Form):
#    a = forms.IntegerField()
#    b = forms.IntegerField()

# Create your views here.
def login_logout_standard(func):
    def wrappser(request,*args,**kwargs):
        user_dict = request.session.get('member_id',None)
        if user_dict:
           return func(request,*args,**kwargs)
        else:
           return redirect('/web/login') 
    return wrappser
def Login(request):
    if request.method == 'POST':
        
        user = request.POST.get('username',None)
        pwd =  request.POST.get('password',None)
       
        status = 'hello'
        
        #检查用户名和密码是否存在，
        b = UserInfo.objects.all()
        print b
        result = UserInfo.objects.filter(username=user,password=pwd).count()
        message = '失败'
        print result
        if result == 1:
            request.session['member_id']= {'user':user}
            return redirect('/web/index/')
        else:
            return render_to_response('login.html', {'hello':b})
        
    else:
        return render_to_response('login.html')
    
def logout(request):
    #销毁session
    del request.session['member_id']
    return redirect('/web/login/')

@login_logout_standard
def index(request):
    #user_dict = request.session.get('member_id',None)
   # if user_dict:  
        #asset_list = Asset.objects.all()
    return render_to_response('index.html',{'username':request.session.get('member_id',None)['user']})
  #  else:
   #     return redirect('/web/login') 
    #把数据嵌套在html中，
    #新字符串返回给用户
    
@login_logout_standard
def machine_add(request):      
   ret = views_hellper. group_fuckid_getValue('Use_by_group')
   ret1 = views_hellper.sqlselect_front('group_list')
   print ret
   ret['group_list']=ret1.get('group_list')
   
  # print ret
  
   # print ret
   if request.method == "POST":
       ip = request.POST.get('ip',None)
       hostname =  request.POST.get('hostname',None)
       develop = request.POST.get('develop',None)
       group = request.POST.get('group',None)
       user_for_group = request.POST.get('user_for_group',None)
       machineadd = machine_list(hostname=hostname,ip_address=ip,Use_by_group=user_for_group,group_list=group,contact_dev=develop)
       machineadd.save()
       
       result = redirect('/web/list')
       
       return result
   else:
       result = render_to_response('add.html',ret)
       return result

    #把数据嵌套在html中，
    #新字符串返回给用户

    
@login_logout_standard
def machine_modify(request):

   
   ip=request.GET.get('ip')
   #print ip
   obj_list = machine_list.objects.get(ip_address=ip)
   
   Use_by_group = obj_list.Use_by_group
   hostname = obj_list.hostname
   group_list = obj_list.group_list
   contact_dev = obj_list.contact_dev
   ret = {'hostname':hostname,'group_list':group_list,'Use_by_group':Use_by_group,'contact_dev':contact_dev,'ip':ip}
   
  
  
   # print ret
   if request.method == "POST":
       #ip_re=request.get.get('ip',None)
       #print ip
       #print request.Get
       hostname_re=request.REQUEST.get('hostname_re',None)
      # print hostname_re
       develop_re=request.REQUEST.get('develop_re',None)
      # print develop_re
       if hostname_re == "":
           hostname_re=hostname
       if develop_re== "":
           develop_re=contact_dev
      # print develop_re
      # print hostname_re
       user_save=machine_list.objects.get(ip_address=ip)
       user_save.hostname=hostname_re
       user_save.contact_dev=develop_re
       user_save.save()
       
       result = redirect('/web/list')
       return result
   else:
       result = render_to_response('machine_change.html',ret)
       return result

    #把数据嵌套在html中，
    #新字符串返回给用户
@login_logout_standard  
def machine(request):
    obj_list = machine_list.objects.values_list('Use_by_group')
    obj_list = obj_list.distinct()
    
    
    obj_list = views_hellper.str_change(obj_list)
    obj_list.pop(0)
    
    
    
   
    pass
    return render_to_response('machadd.html', {'obj_list': obj_list})




@login_logout_standard
def motify_list(request,page):
   # ret = views_hellper.userbygroup()
    #print  ret
    obj_list = machine_list.objects.values_list('Use_by_group')
    obj_list = obj_list.distinct()
    
    
    obj_list = views_hellper.str_change(obj_list)
    #obj_list.pop(0)
   # print 1
   # print obj_list
    ret = {'obj_list': obj_list}
   # print request.POST.has_key
    
    
    if request.method == "POST":
     
        # request.session['group_selected'] = ''
         if request.POST.has_key('user_selected'):
            #print request.POST.get('user_selected')
            
            request.session['group_selected'] = ''
            if request.session['group_selected']=='': 
                 
               #print "hello world"
               user_selected = request.POST.get('user_selected',None)
              
               request.session['group_selected'] = user_selected
              # print request.session['group_selected']
            else:
               pass
            ret=html_helper.page_seg(page,user_selected)
            
            ret['obj_list']= obj_list
           
           
            
         else:
           # print 3
            pass



    else:
        if request.session.has_key('group_selected'):
           #print 1
           # print request.session('group_selected')
            user_selected = request.session['group_selected']
        

            #fuck1=request.post.get('data',None)
            ret=html_helper.page_seg(page,user_selected)
            ret['obj_list']= obj_list
         # print 99
            if request.GET.has_key('dat'):
                
             # print 4
                dat=request.GET.get('dat')
              #  print dat
                machine_list.objects.get(ip_address=dat).delete()
            else:
             #   print 5
                pass
          
        else:
            pass
            print 2
       
    response = render_to_response('machinelist.html',ret)
    return response
    
@login_logout_standard
def ansible_hostsguanli(request):
   # ansible_host_sql=connection.cursor()
  #  print ansible_host_sql
   # fuck = '博雅主站'
  #  ansible_host_sql.execute("""select web_group_fuckid.unic_group,web_machine_list.ip_address  
#    from web_machine_list,web_group_fuckid  where web_machine_list.Use_by_group=web_group_fuckid.Use_by_group AND web_machine_list.Use_by_group=%s""",[fuck])
#
#    print "1"

    
   # obj_list = machine_list.objects.values_list('Use_by_group')
   # obj_list = obj_list.distinct()
   # print obj_list
    #obj_list = machine_list.objects.values('Use_by_group').distinct()
    obj_list = machine_list.objects.values_list('Use_by_group').distinct()
    obj_list = views_hellper.str_change(obj_list)
    #obj_list.pop(0)
    #print obj_list
    ret = {'obj_list': obj_list}
    if request.method == "POST":
     
        # request.session['group_selected'] = ''
         if request.POST.has_key('user_selected'):
            #print request.POST.get('user_selected')
            
        
            user_selected = request.POST.get('user_selected',None)
         
            
            
            
            
            data=models_sql.ansible_host(user_selected)
           # print data
            ret['data']= data
            
         else:
            
            pass



    else:
       pass
    
    
    
   
  #  print ansible_host_sql.fetchall()
    #del request.session['member_id']
    return render_to_response('ansible_hosts.html',ret)



    
    
@login_logout_standard
def ansible_cmd(request):
    obj_list = machine_list.objects.values_list('Use_by_group')
    obj_list = obj_list.distinct()
    
    
    obj_list = views_hellper.str_change(obj_list)
   # obj_list.pop(0)
   # print obj_list
    ret = {'obj_list': obj_list}
    
    if request.method == "POST":
        group=request.POST.get('user_selected',None)
        use_cmd=request.POST.get('user_cmd',None)
        remote_user=request.POST.get('remote_user',None)
        remote_pass=request.POST.get('remote_pass',None)
        hosts=models_sql.ansible_host_getall(group)
       # print hosts
        hosts=views_hellper.str_change(hosts)
       # print hosts
        webInventory = ansible.inventory.Inventory(hosts)

        runner = ansible.runner.Runner(
        module_name='shell',
        module_args=use_cmd,
        #pattern=group,
        forks=5,
        remote_user=remote_user,
        remote_pass=remote_pass,
        #transport='ssh', 
        #sudo='True', 
        sudo='yes',
      
        sudo_pass=remote_pass,
        #transport='ssh',
        #sudo_pass='root',
        #sudo_pass=remote_pass,
        #sudo_user=remote_user,
        inventory=webInventory                            
        ) 
        #print command   
        results  = runner.run() 
        #print results
        #print datastructure
        results_up={}
        results_failed={}
        results_DOWN={}
        
      #  print "UP ***********"
        for (hostname, result) in results['contacted'].items():
            if not 'failed' in result:
                UP_hostname=hostname
                UP_stdout=result['stdout']
                results_up[UP_hostname]=UP_stdout
                #print "%s >>> %s" % (hostname, result['stdout'])

     #   print "FAILED *******"
        for (hostname, result) in results['contacted'].items():
            if 'failed' in result:
                failed_hostname=hostname
                failed_stdout=result['msg']
                results_failed[failed_hostname]=failed_stdout
                #print "%s >>> %s" % (hostname, result['msg'])
     #   print "DOWN *********"
        for (hostname, result) in results['dark'].items():
            DOWN_hostname=hostname
            DOWN_stdout=result
            results_DOWN[DOWN_hostname]=result
          #  print "%s >>> %s" % (hostname, result)
        
        ret['resutls_UP']=results_up
        ret['results_failed']=results_failed
        ret['results_DOWN']=results_DOWN

  
    else:
        pass
    return render_to_response('ansible.html',ret)





@login_logout_standard  
def groupadd(request):
    obj_list = machine_list.objects.values_list('Use_by_group')
    obj_list = obj_list.distinct()
    
    
    obj_list = views_hellper.str_change(obj_list)
   # obj_list.pop(0)
   # print obj_list
    ret = {'obj_list': obj_list}
    if request.GET.has_key('Use_by_group') and request.GET.has_key('unic_group'):
                

    
        Use_by_group=request.POST.get('Use_by_group',None)
        unic_group=request.POST.get('unic_group',None)
        #print Use_by_group
       # print unic_group
        #group_save=group_fuckid(Use_by_group=Use_by_group,unic_group=unic_group)
      
       # group_save.save()
        
    
   

    return render_to_response('ansible_hosts.html',ret)


    
 