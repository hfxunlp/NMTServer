#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import zmq, sys, json

import token
import detoken
import datautils

def _translate_core(jsond):
	sock = zmq.Context().socket(zmq.REQ)
	sock.connect("tcp://127.0.0.1:5556")
	sock.send(jsond)
	return sock.recv()

def _translate(srctext):
	return detoken.detoken(datautils.char2pinyin(datautils.restoreFromBatch(json.loads(_translate_core(json.dumps(datautils.makeBatch(datautils.cutParagraph(token.tokenone(srctext)))))))))

def translate(srctext):
	tmp=srctext.strip()
	if tmp:
		return _translate(tmp)
	else:
		return tmp

def poweron():
	token.poweron()

def poweroff():
	token.poweroff()
