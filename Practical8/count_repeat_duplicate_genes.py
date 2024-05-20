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
            simplified_name = str(re.findall(r'gene:(.+?)\s',gene_name))
            count = gene_sequence.count('GTGTGT')
            if count != 0 and 'duplication' in gene_name:
                f1.write(f"The repeat sequence '{'GTGTGT'}' appears {count} times in the gene '{simplified_name}'."+'\n'+ gene_sequence + '\n')
                simplifed_name = ''
if genes == 'GTCTGT':
    with open('GTCTGT_duplicate_genes.fa','w') as f2:
        for gene_name, gene_sequence in genes_dict.items():
            simplified_name = str(re.findall(r'gene:(.+?)\s',gene_name))
            count = gene_sequence.count('GTCTGT')
            if count !=0 and 'duplication' in gene_name:
                f2.write(f"The repeat sequence '{'GTCTGT'}' appears {count} times in the gene '{simplified_name}'."+'\n'+ gene_sequence + '\n')
                simplified_name = ''




