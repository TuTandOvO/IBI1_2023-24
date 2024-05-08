# The file is composed of one line of gene name and the following lines of gene sequences.
# So it means that the gene name and the gene sequences are one-to-one correspondence.
# So this program uses regex to find out the gene name and gene sequence.
# All of the gene name lines start with '>', we can use it as the decribing sentence.
# And the gene sequence is the following lines.
# It's not hard to think about dictionary.
# Gene name is served as key and gene sequence is served as value.
# When 'GTGTGT' or 'GTCTGT' emerge in the gene sequence, print out the whole gene sequence and its gene name.

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
            genes_dict[gene_name] += line.strip()
genes = input('Please enter your sequences: ')
if genes == 'GTGTGT':
    with open('GTGTGT_duplicate_genes.fa','w') as f1:  
        for gene_name, gene_sequence in genes_dict.items():
            count = gene_sequence.count('GTGTGT')
            if count != 0:
                f1.write(f"The repeat sequence '{'GTGTGT'}' appears {count} times in the gene '{simplified_name}'."+'\n'+ gene_sequence + '\n')
if genes == 'GTCTGT':
    with open('GTCTGT_duplicate_genes.fa','w') as f2:
        for gene_name, gene_sequence in genes_dict.items():
            count = gene_sequence.count('GTCTGT')
            if count !=0:
                f2.write(f"The repeat sequence '{'GTCTGT'}' appears {count} times in the gene '{simplified_name}'."+'\n'+ gene_sequence + '\n')







# origin wrong version
# import re
# genes = input('Please enter your sequences: ')
# s_cerevisiae = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
# s_cerevisiae_text = s_cerevisiae.read().split('\n')
# def prev_line(text, line):
#     index = text.index(line)
#     if index > 0:
#         return text[index - 1]
#     else:
#         return None
# fasta_file_1 = ''
# fasta_file_2 = ''
# count1 = 0
# count2 = 0
# if genes == 'GTGTGT':
#     for line in s_cerevisiae_text:
#         if 'GTGTGT' in line:
#             if prev_line(s_cerevisiae_text,line):
#                 gene_name1 = re.findall(r'gene:.+?\s',prev_line(s_cerevisiae_text,line))
#                 if gene_name1:
#                     fasta_file_1 += 'The GTGTGT ' + str(gene_name1) + '\n'
#                     count1 += 1
#     print(count1)
#     with open('GTGTGT_duplicate_genes.fa','w') as f1:
#         f1.write(fasta_file_1 + '\n')
# if genes == 'GTCTGT':
#     for line in s_cerevisiae_text:
#         if 'GTCTGT' in line:
#             if prev_line(s_cerevisiae_text,line):
#                 gene_name2 = re.findall(r'gene:.+?\s',prev_line(s_cerevisiae_text,line))
#                 if gene_name2:
#                     fasta_file_2 += 'The GTCTGT ' + str(gene_name2) + '\n'
#                     count2 += 1
#     print(count2)
#     with open('GTCTGT_duplicate_genes.fa','w') as f2:
#         f2.write(fasta_file_2 + '\n')

