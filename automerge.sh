#!/bin/sh

unzip -j $1 chrome/tongwen.jar
unzip -j tongwen.jar '*s2t*.js'
sed -e '1,/^$/d' -e 's/"\\u/u"\\u/g' -e 's/TongWen\.//' -e 's/;//' < s2t.js > s2t.py
sed -e '1,/^$/d' -e 's/"\\u/u"\\u/g' -e 's/TongWen\.//' -e 's/;//' < s2t_phrase.js > s2t_phrase.py
./merge.py

rm -f tongwen.jar s2t.js s2t.py s2t.pyc s2t_phrase.js s2t_phrase.py s2t_phrase.pyc
