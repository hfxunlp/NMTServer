#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import zmq, sys, json

import seg
import detoken

def _translate_core(srctext,server):
	sock = zmq.Context().socket(zmq.REQ)
	sock.connect(server)
	sock.send(json.dumps([{"src": srctext}]))
	return sock.recv()

def _translate(srctext):
	if len(srctext)<270:
		full=json.loads(_translate_core(seg.segline(srctext),"tcp://127.0.0.1:5556"))
	#for fu in full:
	#	for ffu in fu:
	#		if "tgt" in ffu:
	#			ffu["tgt"]=detoken.detoken(ffu["tgt"])
		return detoken.detoken(full[0][0].get("tgt",""))
	else:
		return u"未开通断句功能，暂不开放长段翻译。"

def translate(srctext):
	tmp=srctext.strip()
	if tmp:
		return _translate(tmp)
	else:
		return tmp

def open():
	seg.open()

def close():
	seg.close()
