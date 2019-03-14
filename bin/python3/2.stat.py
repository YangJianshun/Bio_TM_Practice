#coding=utf-8
import sys
import os
(cut_txt,step)=sys.argv[1:]
book=cut_txt[:-4]
step=int(step)
#coding=utf-8
#import jieba
#f=open('book','r')
#for line in f:
#    line=line.strip()
#    print(' '.join(jieba.cut(line)))
#f.close()

len_txt=int((list(os.popen('wc -l {}'.format(cut_txt)))[0].split(' '))[0])

o1 = open(book+'.ratio','w')
#o2 = open(book+'.token','w')
for win in range(step,len_txt+step,step):

    f=open(cut_txt,'r')
    i=0;
    words=[];
    for word in f:
        word=word.strip()
        i+=1;
        #print(word)
        words.append(word);
        if i>=win:break;
    f.close()
    if(win>len_txt+step):break
    o1.write('{}\t{}\t{}\n'.format(i,len(set(words))/len(words),len(set(words))))
    #o2.write('{}\t{}\n'.format(i,len(set(words))))

o1.close()
#o2.close()

