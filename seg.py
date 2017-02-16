from pynlpir import nlpir

def segline(strin):
	try:
		rs=nlpir.ParagraphProcess(strin.encode("utf-8","ignore"), 0)
	except:
		rs=""
	return rs.decode("utf-8","ignore")

def open():
	nlpir.Init(nlpir.PACKAGE_DIR,nlpir.UTF8_CODE,None)
	nlpir.SetPOSmap(nlpir.PKU_POS_MAP_SECOND)#ICT_POS_MAP_SECOND/FIRST

def close():
	nlpir.Exit()