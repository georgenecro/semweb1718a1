import csv

s,s2=input("mera,didaskwn\n").split(',')
#s= input('dwse 1')
#s2= input('dwse 2')
# open csv file for reading
with open('programma.csv','r',newline='',encoding='utf-8') as ifp:
	#create csv reader object
	ir = csv.reader(ifp) #defaults to excel 'dialect'   to ir to egrapse reader ston pinaka

	#read first row (headers)
	hdrow = next(ir)

	#iterate over table rows in csv file
	for row in ir:
		#each row is a list of stringsd
		#(table column values for this row)
		if row[0]== s and row[5] == s2 :
			print (row)
		#do something with each row here...
