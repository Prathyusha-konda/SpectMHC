

def install_check(check):
	print "\ncheck"

	netMHC = raw_input('\nDid you install netMHC? reply with yes or no:')

	choice = netMHC.lower()
	
	return choice;


def version(check): 
	
	version = raw_input('\nWhich version of netMHC do you want to use? 4.0 or 3.4 or pan: ')

	if version in ['4.0']:
		print "4.0 is your version"
		
	elif version in ['pan']:
		print "netMHCpan is your version"
	
	elif version in ['3.4']:
		print "3.4 is your version"
	
	return version;


def split_files(split):
	def chunks(l, n):
    		n = max(1, n)
    		return [l[i:i + n] for i in range(0, len(l), n)]
	def new_string(x):
		temp = ">"
		for i in x:
			temp = temp+i+">"
		temp = temp[:-1]
		return temp
	filename = raw_input("\nEnter file name: ")
	number = int(raw_input("\nHow many number of sequences do you want per file? : "))
	split_list=[]


	def mkfile(x,i):
		f = open("split"+str(i)+"_"+filename,"w")
		splitfile='split%s_%s' %(str(i), filename)
		split_list.append(splitfile)
		f.write(x)
		f.close()
	
	

	f = open(filename, "r")
	splitted_file = f.read().split(">")

	new_files = chunks(splitted_file, number)

	count = 1
	for i in new_files:
		q = new_string(i)
		if count == 1:
			q = q[1:]
		mkfile(q,count)
		count=count+1

	return split_list


def executemhc(version, list_of_files):
	
	import datetime
	print datetime.datetime.now()
	import glob, os
	import threading
	
	path = raw_input("\nPlease enter the path to netMHC folder, ex: /home/prathyusha/NetMHC_4.0_for_Linux/netMHC-4.0: ")
	
	num = raw_input("\nPlease enter which length peptides you want to predict; if multiple lengths, seperate numbers with space 8 9 10 11: ")
	input_list = num.split()
	input_list = [int(a) for a in input_list]


	allele=raw_input("\nPlease enter the allele you want to predict; ex- H-2-Kb or HLA-A0301: ")

	out_list = []
	for i in input_list:	
		for filename in list_of_files: 

			head, sep, tail = filename.partition('.f')
			print '\nfile %s is executed' %head 
			
			outfile='%s_%d_output.txt' %(head, i)
			out_list.append(outfile)
			
			if version in '4.0':
				command = '%s/netMHC -l %d -a %s %s > %s' %(path, i, allele, filename, outfile)
			elif version in 'pan':
				command = '%s/netMHCpan -l %d -a %s %s > %s_%d_output.txt' %(path, i, allele, filename, outfile)			
			elif version in '3.4':
				command = '%s/netMHC -l %d -a %s %s > %s' %(path, i, allele, filename, outfile)
			os.system(command)

	print "\nnetMHC execution completed"
	
	return out_list


def process_data(version, filelist, cut_off):
	
	if version in '4.0':
		bad_words = ['high binders', 'iCore', '----', '#']
	
	elif version in 'pan':
		bad_words = ['#', 'training data', 'ICore', 'high binders', '------']

	elif version in '3.4':
		bad_words = ['binder threshold', 'Artificial Neural', 'affinity(nM)', '--------', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

	for filename in filelist:
		newname=filename.replace("output","data")
		print filename
		with open(filename) as oldfile, open(newname, 'w') as newfile:
			for line in oldfile:
				if not any(bad_word in line for bad_word in bad_words):
					if line.strip():
						newline=line.split()
						if version in '3.4':
							if float(newline[3])<cut_off:
								if cut_off<500:
									newfile.write(">>"+newline[5]+"_"+newline[3]+"_"+newline[6]+'\n'+newline[1]+'\n')
								else:
									newfile.write(">>"+newline[4]+"_"+newline[3]+"_"+newline[5]+'\n'+newline[1]+'\n')

						else:

							if float(newline[13])<cut_off:
								newfile.write(">>"+newline[10]+"_"+newline[13]+"_"+newline[1]+'\n'+newline[2]+'\n')

	

	print "\nnetMHC processing complete"



def del_temp_files(list_of_temp_files):
	import os
	for filename in list_of_temp_files:
		os.remove(filename)
	print "\nThe execution is complete. Check your output files in the folder."



