#!/usr/bin/env python
#coding:utf-8

from django.utils.safestring import mark_safe
from web.models import Asset,UserInfo,machine_list
from web import common

class PageInfo:
    
    def __init__(self,current_page,all_count,per_item=5):
        self.CurrentPage = current_page
        self.AllCount = all_count
        self.PerItem = per_item
    @property
    def start(self):
        return  (self.CurrentPage-1)*self.PerItem
    @property
    def end(self):
        return self.CurrentPage * self.PerItem
    @property
    def all_page_count(self):
        temp = divmod(self.AllCount, self.PerItem)
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0] + 1
        return all_page_count
        

def page_seg(page,user_selected):
    
    page = common.try_int(page,1)
    per_item = 5 #设置以5页为分割
    start = (page-1)*5
    end = page*5
    
    
    
    count = machine_list.objects.filter(Use_by_group=user_selected).count()
    #count = machine_list.objects.all().count()

    #result = machine_list.objects.all()[start:end]
    result = machine_list.objects.filter(Use_by_group=user_selected)[start:end]


    all_pages_temp = divmod(count,per_item)
    
    if all_pages_temp[1] == 0:
        all_pages = all_pages_temp[0]
    else:
        all_pages = all_pages_temp[0]+1
        
    older_page = page -1
    newer_page = page +1
        
    
    page_html = []
    first_html = "<li><a href='/web/list/%d'>首页</a></li>"  %(1,)
    page_html.append(first_html)
    #上一页逻辑设置
    if page <= 1:
        older_html = "<li><a href='/web/list/#'>上页</a></li>"
    else: 
        older_html = "<li><a href='/web/list/%d'>上页</a></li>"  %(older_page,)
    page_html.append(older_html)
    
    if all_pages <5:
        begin = 0
        end = all_pages
    else:
        if page<5:
            begin = 0
            end = 6
        else:
            if page + 3 > all_pages:
                begin = page -3
                end = all_pages
            else:
                begin = page -3
                end = page +2
                 
    for i in range(begin,end):  #i从0开始循环
        if page == i+1:
             a_html =  "<li><a class='dropdown open' href='/web/list/%d'>%d</a></li>"   %(i+1,i+1)
        else:
            a_html =  "<li><a  href='/web/list/%d'>%d</a></li>"   %(i+1,i+1)
        page_html.append(a_html)
    #下一页
    if page+1 > all_pages:
        newer_html = "<li><a href='/web/list/#'>上页</a></li>"    
    else:
        newer_html =  "<li><a href='/web/list/%d'>下页</a></li>"  %(newer_page,)       
    page_html.append(newer_html)       
    
    end_html =  "<li><a href='/web/list/%d'>尾页</a></li>"  %(all_pages,)       
    page_html.append(end_html)
    
    page = mark_safe("".join(page_html)) 
    #print result
    ret = {'shuju':result,'count':count,'page':page}
    return ret
    #ret = {'shuju':result,'count':count,'page':page,'obj_list': obj_list}
    