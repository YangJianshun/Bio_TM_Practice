# -*- coding: utf-8 -*-
import sys
import jieba

book=sys.argv[1]
f=open(book,'r')
o=open(book+'.cut','w')
biaodian='^×=>-,:/.......·\'‘’"“”()[]*+±。《》：，…、；—―？！?!-·~|（）& \t'

for line in f:
    line=line.strip()
    if line=='': continue
    o.write('\n'.join([x for x in jieba.cut(line) if not x in biaodian]))
    o.write('\n')
f.close()
o.close()
