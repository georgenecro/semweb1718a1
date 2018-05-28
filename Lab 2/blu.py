import csv

#s,s2=input("mera,didaskwn\n").split(',')
#s= input('dwse 1')
#s2= input('dwse 2')
# open csv file for reading
with open('programma.csv','r',newline='',encoding='utf-8') as ifp:
	with open('out.csv','w',newline='') as ofp:
		ir = csv.reader(ifp)
		writer = csv.writer(ofp)
		#create csv reader object
	

		#read first row (headers)
		hdrow = next(ir)

		#iterate over table rows in csv file
		for i,row in enumerate(ir):
			for j,item in enumerate(row):

				if hdrow [j] == 'ΕΝΑΡΞΗ' or hdrow[j] == 'ΛΗΞΗ' or  hdrow [j] == 'ΗΜΕΡΑ':
					writer.writerow (['b:'+str(i+1),hdrow[j],'l:' + item])
				else: 
					writer.writerow (['b:'+str(i+1),hdrow[j],'u:' + item])
				#writer.writerow([i+1,hdrow[j],item])
			#each row is a list of stringsd
			#(table column values for this row)
		
			#do something with each row here...
