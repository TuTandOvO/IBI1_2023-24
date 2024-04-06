import re
s_cerevisiae = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
s_cerevisiae_text = s_cerevisiae.read().split('\n')
fasta_file = ''
for line in s_cerevisiae_text:
    if line.startswith('>') and 'duplication' in line:
        gene_name = re.findall(r'gene:.+?\s',line)
        fasta_file += 'The duplicated ' + str(gene_name) + '\n'
with open('duplicate_genes.fa','w') as f:
    f.write(fasta_file+'\n')

# First import regex tool
# Read the file use read() and split lines based on '\n' symbol
# In the for loops, first we pick up the decribing sentences and find out which contain 'duplication'
# In correct line, use regex (findout statement) to find out the gene name 
# Findout can turn strings into list
# But only strings can be written into files, we need to use str() to turn list into strings

    

