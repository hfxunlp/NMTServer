# -*- coding:utf-8 -*-
import os
import sys
import re

zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
enPattern = re.compile(u"[A-Za-z0-9]")

def ldpunc(fname):
	f=open(fname)
	r=f.read()
	f.close()
	r=r.decode("utf-8")
	r=r.strip()
	r=" ".join(r)
	r=r.split(" ")
	r=set(r)
	r.remove("")
	return list(r)

def npunc(strin):
	global puncPattern
	rs=True
	for pu in puncPattern:
		if strin.find(pu)>=0:
			rs=False
			break
	return rs

'''
def npunc(strin):
	global puncPattern
	if puncPattern.search(strin):
		return False
	else:
		return True
'''

def mkbool(din):
	if din:
		return True
	else:
		return False

def ncomb(strin):
	global zhPattern, enPattern
	return mkbool(zhPattern.search(strin))^mkbool(enPattern.search(strin))

def fillwd(strin):
	if len(strin)<7 and strin.find(u"的")==-1 and len(strin)>2 and npunc(strin) and ncomb(strin):
		return True
	else:
		return False

def filter(strin):
	return fillwd(strin)
	#return True
	#return npunc(strin)

def makedict(prod,rsf):
	dadd=set([])
	with open(prod) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8")
				tmp=tmp.split("|||")
				if len(tmp)==2:
					tmp=tmp[0]
					if not tmp in dadd:
						if filter(tmp):
							dadd.add(tmp)
	with open(rsf,"w") as fwrt:
		fwrt.write("\n".join(dadd).encode("utf-8"))

if __name__ == '__main__':
	puncPattern=ldpunc("punc.txt")
	makedict(sys.argv[1].decode("gbk"),sys.argv[2].decode("gbk"))