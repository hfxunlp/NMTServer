from nltk.tokenize.moses import MosesDetokenizer
detokenizer = MosesDetokenizer()

def detoken(strin):
	try:
		rs=detokenizer.detokenize(strin.split(" "), return_str=True)
	except:
		rs=""
	return rs
