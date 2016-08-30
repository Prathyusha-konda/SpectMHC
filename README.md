# netMHC_DB_scripts


1. The code provided here is used to create MHC peptide database using netMHC software. 

2. You will need to install offline version of netMHC -4.0 or 3.4 or pan versions onto your Ubuntu or Darwin system. The instructions for istallation are provided on the netMHC website. 

3. Please download the SpectMHC_main.py, SpectMHC_methods.py, readme file and keep them in the same folder as your "parent file". The folder can be present anywhere on the system.

4. Parent file is supposed to be in fasta file format. 

5. Once you are successful with installing netMHC, and ready with your parent and code files, open terminal from the folder containing your parent file, and enter

>>python SpectMHC_main.py

6. This command executes the SpectMHC_main.py file, which is depended on SpectMHC_methods.py, so make sure you have them together.

7. Once you execute the main.py file, you will get instructions on the terminal, please look at the examples that appear on the screen for better understanding. 

8. You can choose to work with either netMHC-4.0/3.4 or pan versions. Please choose the specific version when you are asked for on the screen.

9. NetMHC software allows the user to execute files with "At most 5000 sequences per submission; each sequence not more than 20,000 amino acids and not less than 8 amino acids". Please make sure that you abide by their rules. 

10. If you have a file input with more than 5000 sequences or more than 20,000 amino acids, when prompted if you want to split the file, please choose yes and input the no of sequences that you want in each split file. If you are dealing with big data, we would suggest you to split the file such that you have <=1000 sequences in order to reduce the processing time per file. 

11. For queries related to the tool, please contact:
    prathyusha.konda@dal.ca



