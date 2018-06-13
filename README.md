#SpectMHC Tool

-> The code provided here is used to create MHC peptide databases using netMHC software.
To download the files, open the files, click on 'Raw' at the top, right click on the browser, Save as - save!

-> You will need to install the offline version of netMHC -4.0 or 3.4 or pan onto your Ubuntu or Darwin system. The instructions for installation are provided on the netMHC website:

http://www.cbs.dtu.dk/cgi-bin/nph-sw_request?netMHC

-> Download the SpectMHC_main.py, SpectMHC_methods.py, and .readme file and keep them in the same folder as your "parent file" (fasta file you which to predict from). The folder can be present anywhere on the system .

-> Once you are successful with installing netMHC, and ready with your parent and code files, open terminal from the folder containing your parent file and enter:

>>python SpectMHC_main.py

-> This command executes the SpectMHC_main.py file, which is depended on SpectMHC_methods.py, so make sure you have them together.

-> Once you execute the main.py file, you will get instructions on the terminal. Look at the examples that appear on the screen for a better understanding.

-> You can choose to work with either netMHC-4.0/3.4 or pan versions. Just choose the specific version when you are prompted.

-> You will be prompted to split your file, but it is #not mandatory to split your file. 
However, if you split the file, it will be easier to navigate incase your computer or program hangsup on you. If you decide to split your file, you can split into 5000-10000 sequences per file.


#For queries related to the tool, please contact:
#    prathyusha.konda@dal.ca




