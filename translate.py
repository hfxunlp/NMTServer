#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import zmq, sys, json

import seg
import detoken

def translate_core(srctext,server):
	sock = zmq.Context().socket(zmq.REQ)
	sock.connect(server)
	sock.send(json.dumps([{"src": srctext}]))
	return sock.recv()

def translate(srctext):
	full=json.loads(translate_core(seg.segline(srctext),"tcp://127.0.0.1:5556"))
	for fu in full:
		for ffu in fu:
			if "tgt" in ffu:
				ffu["tgt"]=detoken.detoken(ffu["tgt"])
	return full[0][0]["tgt"]

def open():
	seg.open()

def close():
	seg.close()
