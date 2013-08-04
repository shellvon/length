#!usr/bin/env python
# Created at 2013-8-4
# Written by shellvon

file=open('input.txt')
dic={}
for line in file:
	if line.count('='):
		a,frm,_,to,m=line.split()
		dic[frm]=float(to)/float(a)
	else:
		break
dic['feet']=dic['foot']
keys=dic.keys()
with open('output.txt','wb') as f:
	f.write('iamshellvon@gmail.com\n\n')
for line in file:
	for x in keys:
		line=line.replace(x,"*%s"%dic[x])
	line=line.replace('e','')
	line=line.replace('s','')
	with open('output.txt','a') as f:
		f.write("%.2f m\n"%float(eval(line)))
