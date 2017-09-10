from pynlpir import nlpir
import os

def tokenone(strin):
	try:
		rs=nlpir.ParagraphProcess(strin.encode("utf-8","ignore"), 0)
	except:
		rs=""
	return rs.decode("utf-8","ignore")

def ImDict(fname):
	with open(fname) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8")
				if tmp:
					nlpir.AddUserWord(tmp.encode("utf-8"))

def poweron():
	nlpir.Init(nlpir.PACKAGE_DIR,nlpir.UTF8_CODE,None)
	#nlpir.SetPOSmap(nlpir.ICT_POS_MAP_SECOND)#ICT_POS_MAP_SECOND/FIRST
	if os.path.exists("segdict.txt") and os.path.isfile("segdict.txt"):
		ImDict("segdict.txt")

def poweroff():
	nlpir.Exit()
