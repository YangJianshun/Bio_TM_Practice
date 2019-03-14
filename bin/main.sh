#!/usr/bin/bash
TEXT=$1
if [ $# != 1  ] ;then
echo 'USAGE $0 <TXT_FILE>'
exit
elif [ ! -e $1 ] ;then
echo '[Error] '$1' not exists!'
exit
fi
#判断$1是否存在

STEP=5000
#画token图的时候移动的单位，多少词，可以在这里修改

PYTHON_VERSON=`python --version 2>&1 | awk -F ' ' '{print $2}' | cut -d . -f 1`
#检查python版本，由于编码问题python2和python3不好兼容，这里我写了两个版本的python脚本

if [ $PYTHON_VERSON == 2 ]
then
echo 'python2'
BIN=$(cd `dirname $0`'/python2/' ; pwd)
echo $BIN
elif [ $PYTHON_VERSON == 3 ]
then
echo 'python3'
BIN=$(cd `dirname $0`'/python3/' ; pwd)
echo $BIN
else
echo 'Unable to determine your python version'
fi

#--------主要部分----------
python $BIN/1.cut.py $TEXT
python $BIN/2.stat.py $TEXT.cut $STEP
python $BIN/3.draw_ratio.py $TEXT.ratio
python $BIN/4.stat_freq.py $TEXT.cut $BIN/../StopWords.txt
#生成一个R脚本，可以用Rstdio打开
echo '
library(wordcloud2)
wf<-read.table("'$(readlink -f $TEXT)'.freq" , fileEncoding = "UTF-8")
wordcloud2(subset(wf,V2>300))
' > $TEXT.R

