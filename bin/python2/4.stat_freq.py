#conding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

cut_txt,StopWords_txt=sys.argv[1:]
S=open(StopWords_txt,'r')
StopWords = [x.strip() for x in S]
S.close()
f=open(cut_txt,'r')
book=cut_txt[:-4]
o=open(book+'.freq','w')
num={};
for word in f:
    word=word.strip()
    if word in StopWords: continue
    num.setdefault(word,0)
    num[word]+=1;
f.close()
words=sorted(num.keys(),key=lambda x:num[x],reverse=True)
for word in words:
    o.write("{}\t{}\n".format(word,num[word]))
o.close()
