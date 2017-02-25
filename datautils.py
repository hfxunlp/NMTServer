#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

splitcode=set([u"。", u"？", u"！", u"；", u"\n"])

def cutParagraph(strin):
	global splitcode
	rs=[]
	ind=0
	lind=0
	for stru in strin:
		if stru in splitcode:
			rs.append(strin[lind:ind+1])
			ind+=1
			lind=ind
		else:
			ind+=1
	if lind<ind:
		rs.append(strin[lind:])
	return rs

def makeBatch(srcl):
	rs=[]
	for srcu in srcl:
		tmp=srcu.strip()
		if tmp:
			rs.append({"src":tmp})
	return rs

def restoreFromBatch(transl):
	rs=[]
	for tranu in transl:
		tmp=tranu[0]
		if type(tmp)==dict:
			tmp=tmp.get("tgt","")
			if tmp:
				rs.append(tmp)
	return " ".join(rs)