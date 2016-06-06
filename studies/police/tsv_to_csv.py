from sys import argv,exit

if len(argv)!=3:
	print "Usage: python tsv_to_csv.py input.tsv output.csv"
	exit(2)

input_filename = argv[1]
output_filename = argv[2]

output = ""
with open(input_filename) as infile:
    for line in infile:
        line = line.replace(" ","")
        line = line.replace("\t\t\t\t","\t")
        line = line.replace("\t\t\t","\t")
        line = line.replace("\t\t","\t")
        line = line.replace("\t",",")
	output+=line
with open(output_filename,'w') as outfile:
    outfile.write(output)
    
