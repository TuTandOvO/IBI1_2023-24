# Use dictionary tool to math gene name and gene sequences
# Use regex function to find gene name line which have duplication and extract gene name
# Use dictionary tool to store gene sequence
# Write gene name and its sequence to a file
import re
fasta_file_path = r'D:\IBI\IBI1_2023-24\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
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











    

