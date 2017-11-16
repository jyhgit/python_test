#!/usr/bin/env python
# -*- coding: utf-8 -*-
#auth :jyh
import  sys
try:
	import libvirt
	HAS_LIBVIRT=True
except Exception:
	HAS_LIBVIRT=False
def is_virtual():
	"""
	判断当前系统是不是支持虚拟化
	"""
	if not HAS_LIBVIRT:
		sys.exit("current system not support virt")
	return 'virt'
def	 get_conn():
	'''
	获取libvirt连接句柄，用户提供libvirt接口
	'''
	if is_virtual() == 'virt':
		try:
			conn=libvirt.open('qeum:///system')
		except Exception as e:
			sys.exit(e)
	return conn

def close_conn(conn):
	'''
	关闭conn 连接
	:param conn:
	:return:
	'''
	return conn.close()
def list_active_vms():
	'''
	列出所有
	:return:
	'''
	vms_list=[]
	conn=get_conn()
	doamin_list=conn.listDoaminsID()
	for id in doamin_list:
		vms_list.append(conn.lookupByID(id).name())
	close_conn(conn)
	return vms_list
def list_inactive_vms():
	'''
	列出关闭的机器
	:return:
	'''
	vms_list=[]
	conn=get_conn()
	for id in conn.listDefinedDomains():
		vms_list.append(id)
	close_conn(conn)
	return vms_list
def list_all_vms():
	'''

	:return:
	'''
	vms=[]
	vms.extend(list_active_vms())
	vms.extend(list_inactive_vms())
	return vms
def get_capability():
	'''

	:return:
	'''
	conn=get_conn()
	capability=conn.getCapabilities()
	conn.close()
	return capability
def get_hostname:
	'''

	:return:
	'''
	conn=get_conn()
	hostname=conn.getHostname()
	conn.close()
	return hostname
def get_max_vcpus():
	'''

	:return:
	'''
	conn=get_conn()
	max_vcpus=conn.getMaxVcpus(None)
	conn.close()
	return max_vcpus
if __name__ == "__main__":
	print "当前主机%s的虚拟机列表:"%(get_hostname())
	for vms in list_active_vms():
		print vms

