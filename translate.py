#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import zmq, sys, json

import seg
import detoken
import datautils

def _translate_core(jsond):
	sock = zmq.Context().socket(zmq.REQ)
	sock.connect("tcp://127.0.0.1:5556")
	sock.send(jsond)
	return sock.recv()

def _translate(srctext):
	return detoken.detoken(datautils.restoreFromBatch(json.loads(_translate_core(json.dumps(datautils.makeBatch(datautils.cutParagraph(seg.segline(srctext))))))))

def translate(srctext):
	tmp=srctext.strip()
	if tmp:
		return _translate(tmp)
	else:
		return tmp

def poweron():
	seg.poweron()

def poweroff():
	seg.poweroff()
