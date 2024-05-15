# Use dictionary tool to math gene name and gene sequences
# Use regex function to find gene name line which have duplication and extract gene name
# Use dictionary tool to store gene sequence
# Write gene name and its sequence to a file
import re
fasta_file_path = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
genes_dict = {}
with open(fasta_file_path, 'r') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):
            gene_name = line
            genes_dict[gene_name] = ""
            simplified_name = str(re.findall(r'gene:(.+?)\s',line))
        else:
            genes_dict[gene_name] += line
with open('duplicate_genes.fa','w') as f1:  
        for gene_name, gene_sequence in genes_dict.items():
            count = gene_name.count('duplication')
            if count !=0:
                f1.write( simplified_name+'\n'+ gene_sequence + '\n')








#origin version (not correct)
# import re
# s_cerevisiae = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
# s_cerevisiae_text = s_cerevisiae.read().split('\n')
# fasta_file = ''
# for line in s_cerevisiae_text:
#     if line.startswith('>') and 'duplication' in line:
#         gene_name = re.findall(r'gene:.+?\s',line)
#         fasta_file += 'The duplicated ' + str(gene_name) + '\n'
# with open('duplicate_genes.fa','w') as f:
#     f.write(fasta_file+'\n')

# First import regex tool
# Read the file use read() and split lines based on '\n' symbol
# In the for loops, first we pick up the decribing sentences and find out which contain 'duplication'
# In correct line, use regex (findout statement) to find out the gene name 
# Findout can turn strings into list
# But only strings can be written into files, we need to use str() to turn list into strings

    

