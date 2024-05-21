# The file is composed of one line of gene name and the following lines of gene sequences.
# So it means that the gene name and the gene sequences are one-to-one correspondence.
# So this program uses regex to find out the gene name and gene sequence.
# All of the gene name lines start with '>', we can use it as the decribing sentence.
# And the gene sequence is the following lines.
# It's not hard to think about dictionary.
# Gene name is served as key and gene sequence is served as value.
# When 'GTGTGT' or 'GTCTGT' emerge in the gene sequence, print out the whole gene sequence and its gene name.

import re
fasta_file_path = r'D:\IBI\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
genes_dict = {}

def count_1(string):
    counter = 0
    for i in range(0, len(string)-1):
        substring = string[i:i+6]  
        if substring == 'GTGTGT':
            counter += 1
    return counter

def count_2(string):
    counter = 0
    for i in range(0, len(string)-1):
        substring = string[i:i+6]  
        if substring == 'GTCTGT':
            counter += 1
    return counter

with open(fasta_file_path, 'r') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):
            gene_name = line
            genes_dict[gene_name] = ""
        else:
            genes_dict[gene_name] += line.strip()
genes = input('Please enter your sequences: ')
if genes == 'GTGTGT':
    with open('GTGTGT_duplicate_genes.fa','w') as f1:  
        for gene_name, gene_sequence in genes_dict.items():
            simplified_name = str(re.findall(r'>(.+?)\s',gene_name))
            count = count_1(gene_sequence)
            if count != 0 and 'duplication' in gene_name:
                f1.write(f" {count}  {simplified_name}"+'\n'+ gene_sequence + '\n')
                simplifed_name = ''
if genes == 'GTCTGT':
    with open('GTCTGT_duplicate_genes.fa','w') as f2:
        for gene_name, gene_sequence in genes_dict.items():
            simplified_name = str(re.findall(r'>(.+?)\s',gene_name))
            count = count_2(gene_sequence)
            if count !=0 and 'duplication' in gene_name:
                f2.write(f" {count} {simplified_name}"+'\n'+ gene_sequence + '\n')
                simplified_name = ''



