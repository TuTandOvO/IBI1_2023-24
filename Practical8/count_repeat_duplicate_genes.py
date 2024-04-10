# import re
# genes = input('Please enter your sequences: ')
# s_cerevisiae = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
# s_cerevisiae_text = s_cerevisiae.read().split('\n')
# def next_line(text, line):
#     index = text.index(line)
#     return text[index + 1]
# fasta_file_1 = ''
# fasta_file_2 = ''
# count = 0
# if genes == 'GTGTGT':
#     for line in s_cerevisiae_text:
#         if line.startswith('>'):
#             gene_name1 = re.findall(r'gene:.+?\s',line)
#             if 'GTGTGT' in line:
#                 count += line.count('GTGTGT')
#                 if next_line(s_cerevisiae_text,line).startswith('>') and count !=0:
#                     if gene_name1:
#                         fasta_file_1 += 'The GTGTGT ' + str(gene_name1) + str(count)+ '\n'
#                         count = 0
#     with open('GTGTGT_duplicate_genes.fa','w') as f1:
#         f1.write(fasta_file_1 + '\n')
# if genes == 'GTCTGT':
#     for line in s_cerevisiae_text:
#         if 'GTCTGT' in line:
#             if next_line(s_cerevisiae_text,line):
#                 gene_name2 = re.findall(r'gene:.+?\s',next_line(s_cerevisiae_text,line))
#                 if gene_name2:
#                     fasta_file_2 += 'The GTCTGT ' + str(gene_name2) + '\n'
#     with open('GTCTGT_duplicate_genes.fa','w') as f2:
#         f2.write(fasta_file_2 + '\n')




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


import re
fasta_file_path = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
genes_dict = {}
with open(fasta_file_path, 'r') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):
            gene_name = str(re.findall(r'gene:.+?\s',line))
            genes_dict[gene_name] = ""
        else:
            genes_dict[gene_name] += line.strip()
genes = input('Please enter your sequences: ')
if genes == 'GTGTGT':
    with open('GTGTGT_duplicate_genes.fa','w') as f1:  
        for gene_name, gene_sequence in genes_dict.items():
            count = gene_sequence.count('GTGTGT')
            if count !=0:
                f1.write(f"The repeat sequence '{'GTGTGT'}' appears {count} times in the gene '{gene_name}'."+'\n'+ gene_sequence + '\n')
if genes == 'GTCTGT':
    with open('GTCTGT_duplicate_genes.fa','w') as f2:
        for gene_name, gene_sequence in genes_dict.items():
            count = gene_sequence.count('GTCTGT')
            if count !=0:
                f2.write(f"The repeat sequence '{'GTCTGT'}' appears {count} times in the gene '{gene_name}'."+'\n'+ gene_sequence + '\n')

