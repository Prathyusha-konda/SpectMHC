import SpectMHC_methods

if SpectMHC_methods.install_check("verify") in 'yes':
	print "\nOk, Let's move ahead"
	version = SpectMHC_methods.version("verify version")
	split_output=raw_input("\nDo you want to split your parent file? yes or no: ")
	if split_output in 'yes':
		split_list=SpectMHC_methods.split_files("split")
		check1 = raw_input("\nDo you want to save your splitfiles after we complete the execution? yes or no: ")
		check2 = raw_input("\nDo you want the output in fasta format? note: this includes processing after netMHC output, yes or no: ") 
			

		if check2 in 'yes':
			if version in '3.4':
				cut_off=float(raw_input("\nWhat is the binding affinity cut_off you are interested in? netmhc suggests 50 for strong binders and 500 for weak binders: "))
			else:
				cut_off=float(raw_input("\nWhat is the cut_off Rank you are interested in? netMHC suggests cutoff rank of 0.5 for strong binders and 2 for weak binders: "))			

			check3 = raw_input("\nDo you want to save your raw netMHC output files along with the fasta output? yes or no: ")

			outfile_list=SpectMHC_methods.executemhc(version, split_list)
  
			print "\nWait while your data is processed into fasta format..."
			if check1 in 'no':
				SpectMHC_methods.del_temp_files(split_list)
			elif check1 in 'yes':
				print "\nSplit files are saved to your computer..."

			if check2 in 'yes':
				SpectMHC_methods.process_data(version, outfile_list, cut_off)

			if check3 in 'yes':
				print "\nThe execution is complete. Check your output files in the folder..."
			elif check3 in 'no':
				SpectMHC_methods.del_temp_files(outfile_list)

		elif check2 in 'no':
			
			SpectMHC_methods.executemhc(version, split_list)
	
			if check1 in 'no':
				SpectMHC_methods.del_temp_files(split_list)
			elif check1 in 'yes':
				print "\nSplit files are saved to your computer..."		
 

	elif split_output in 'no':
		files = raw_input("\nPlease enter your file names, if you have multiple files, separate them by space. ex- 1.fsa 2.fsa 3.fsa: ")
		input_files = files.split()
			
		
		check2 = raw_input("\nDo you want the output in fasta format? yes or no: ") 
		if check2 in 'yes':
			if version in '3.4':
				cut_off=float(raw_input("\nWhat is the binding affinity cut_off you are interested in? netmhc suggests 50 for strong binders and 500 for weak binders: "))
			else:
				cut_off=float(raw_input("\nWhat is the cut_off Rank you are interested in? netMHC suggests cutoff rank of 0.5 for strong binders and 2 for weak binders : "))			
			check3 = raw_input("\nDo you want to save your raw netMHC output files along with the fasta output? yes or no: ")
			file_list=SpectMHC_methods.executemhc(version, input_files)
		
			print "\nWait while your data is processed into fasta format"
			
			if check2 in 'yes':			
				SpectMHC_methods.process_data(version, file_list, cut_off)
			
			if check3 in 'yes':
				print "\nThe execution is complete. Check your output files in the folder."
			elif check3 in 'no':
				SpectMHC_methods.del_temp_files(file_list)
				

		elif check2 in 'no':
			SpectMHC_methods.executemhc(version, input_files)
		
			
	
			
