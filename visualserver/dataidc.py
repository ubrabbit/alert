# -*- coding:utf-8 -*-
'''
Created on 2016-4-25
@author: admin
算法：
	将给定的IP算出所属于的网段，然后找到这个网段的接入口和交换机IP
'''

HZ_DICT={
		'name':'惠州',
		'abbr':'HZ',
		'info':[
					{
						#'abbr':'dx',
						'name':'惠州电信-1',
						'ip':'113.106.204.130',
						'ethernet':'GigabitEthernet0/28',
						'bound':'1000',
					},
					{
						#'abbr':'dx',
						'name':'惠州电信-2',
						'ip':'113.106.204.126',
						'ethernet':'GigabitEthernet0/48',
						'bound':'1000',
					},
		]
	}

SD_DICT={
		'name':'顺德',
		'abbr':'SD',
		'info':[
					{
						#'abbr':'dx',
						'name':'顺德电信-1',
						'ip':'183.60.198.126',
						'ethernet':'GigabitEthernet0/24',
						'bound':'1000',
					},
		]
	}

SY_DICT={
		'name':'沈阳',
		'abbr':'SY',
		'info':[
					{
						#'abbr':'lt',
						'name':'沈阳联通-1',
						'ip':'124.95.140.60',
						'ethernet':'GigabitEthernet0/24',
						'bound':'1000',
					}
		]
	}

JN_DICT={
		'name':'济南',
		'abbr':'JN',
		'info':[
					{
						#'abbr':'lt',
						'name':'济南联通-1',
						'ip':'123.129.209.97',
						'ethernet':'GigabitEthernet0/24',
						'bound':'500',
					},
					{
						#'abbr':'lt',
						'name':'济南联通-３',
						'ip':'119.188.15.160',
						'ethernet':'GigabitEthernet0/24',
						'bound':'500',
					},
		]
	}

FS_DICT={
		'name':'佛山',
		'abbr':'FS',
		'info':[
					{
						#'abbr':'dx',
						'name':'佛山10G-core',
						'ip':'219.132.195.1',
						'ethernet':'TenGigabitEthernet1/1',
						'bound':'4000',
					},
					{
						#'abbr':'lt',
						'name':'佛山10G-联通',
						'ip':'219.132.195.1',
						'ethernet':'TenGigabitEthernet1/3',
						'bound':'500',
					},
		]
	}

ZS_DICT={
		'name':'中山',
		'abbr':'ZS',
		'info':[
					{
						'name':'中山双线-１',
						'ip':'183.61.80.237',
						'ethernet':'GigabitEthernet1/0/52',
						'bound':'1000',
					},
					{
						'name':'中山双线-3',
						'ip':'183.61.86.5',
						'ethernet':'GigabitEthernet1/0/28',
						'bound':'1000',
					},
					{
						#'abbr':'dx',
						'name':'中山10G-core',
						'ip':'121.201.102.1',
						'ethernet':'TenGigabitEthernet1/1',
						'bound':'3000',
					},
		]
	}

CZ_DICT={
		'name':'常州',
		'abbr':'CZ',
		'info':[
					{
						'name':'常州电信',
						'ip':'112.73.64.1',
						'ethernet':'TenGigabitEthernet1/32',
						'bound':'3000',
					},
					{
						'name':'常州联通',
						'ip':'112.73.64.1',
						'ethernet':'TenGigabitEthernet1/30',
						'bound':'500',
					},
		]
	}

XG_DICT={
		'name':'香港',
		'abbr':'XG',
		'info':[
					{
						'name':'香港',
						'ip':'218.213.229.66',
						'ethernet':'GigabitEthernet1/0/24',
						'bound':'100',
					}
		]
	}

GYD_DICT={
		'name':'南方基地',
		'abbr':'GYD',
		'info':[
					{
						'name':'南方基地',
						'ip':'183.232.9.1',
						'ethernet':'XGigabitEthernet0/0/1',
						'bound':'500',
					}
		]
	}
IDC_LIST=[HZ_DICT,SD_DICT,SY_DICT,JN_DICT,FS_DICT,ZS_DICT,CZ_DICT,XG_DICT,GYD_DICT]

################################################################
#上面是一个完成的结构化数据，下面就可以通过计算来得到部分配置，这样能使数据容易维护
#
################################################################
Node_List=[]					#这个列表能让逻辑代码不再使用循环for查询，提高效率和可维护性
for IdcDict in IDC_LIST:
	Node_List+=IdcDict['info']
