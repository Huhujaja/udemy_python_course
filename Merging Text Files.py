'''Coding Exercise 6: Merging Text Files'''

import datetime

filename=datetime.datetime.now()

lst=["file1.txt","file2.txt","file3.txt"]

for files in lst:
	with open(files,'r') as threefile:
		content=threefile.read()
		with open(filename.strftime("%Y-%m-%d-%H-%M")+'.txt','a+') as file:
			file.write(content+"\n")

