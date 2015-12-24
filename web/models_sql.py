#!/usr/bin/env python
#coding:utf-8
from django.db import models,connection


def ansible_host(fuck):
    ansible_host_sql=connection.cursor()
    ansible_host_sql.execute("""select web_group_fuckid.unic_group,web_machine_list.ip_address  
    from web_machine_list,web_group_fuckid  where web_machine_list.Use_by_group=web_group_fuckid.Use_by_group AND web_machine_list.Use_by_group=%s""",[fuck])
    return ansible_host_sql.fetchall()
def ansible_host_getall(fuck):
    ansible_host_sql=connection.cursor()
    ansible_host_sql.execute("""select web_machine_list.ip_address  
    from web_machine_list,web_group_fuckid  where web_machine_list.Use_by_group=web_group_fuckid.Use_by_group AND web_machine_list.Use_by_group=%s""",[fuck])
    return ansible_host_sql.fetchall()