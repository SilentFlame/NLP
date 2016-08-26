import re
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
            r"(https?:\/\/)?([\w\-]+\.)?[\w\-]+\.[\w]{2,6}([\/\?][\w\-\!\?\%\~\&\=\+]+[\.]?[\w\-\!\?\%\~\&\=\+]*)*\/?",   #URL's
            r"[\w]+\-[\w]+",          # HYPHEN
            r"[\w]+\'[\w]+",          #APOSTROPHE  
            r"([A-Z][\s]?[\.]?[\s]){3,8}",        
            r"@([A-Za-z0-9_]+\:)",       #WRITER/MENTION
            r"([\<\>\}]?[\:\;B][\'\"]?[\-\^]?[\)\(\#\@\$SPpdDOoL\|\/\\]{1,3})|([\)\(\#\@\$dOo\|\/\\]{1,3}[\-\^]?[\'\"]?[\:][\<\>\{E]?)",   #EMOTICONS
            r"[a-zA-Z]+",  
            r"[^\s\,\?\!\-\_\:\"\'\;]+",
            r"[^\s]",
            r"\s+",
            r"(mailto:)?[^\s]+@[^\s]+\.[\w]{2,6}",
            r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",
            r"<[^>]+>"
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
f1 = open('twitter_data.txt', 'r')
f2 = open('tokened_result.txt', 'wa')
varLine = f1.read()

tweets = varLine.split('\n')
for tweet in tweets:
	l=(preprocess(tweet))
	f2.write("[")
    	for l1 in l:
		if l1[0]!=" ":
			f2.write("'")
       			f2.write(l1[0])
			f2.write("'")
		f2.write(" ")	
	f2.write('\n')

f1.close()
f2.close()
