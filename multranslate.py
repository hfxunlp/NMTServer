#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import zmq, sys, json

import seg
import detoken
import datautils

from random import sample

serverl=["tcp://127.0.0.1:"+str(port) for port in xrange(5556,5556+4)]

def _translate_core(jsond):
	global serverl
	sock = zmq.Context().socket(zmq.REQ)
	sock.connect(sample(serverl, 1)[0])
	sock.send(jsond)
	return sock.recv()

def _translate(srctext):
	return detoken.detoken(datautils.char2pinyin(datautils.restoreFromBatch(json.loads(_translate_core(json.dumps(datautils.makeBatch(datautils.cutParagraph(seg.segline(srctext)))))))))

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
