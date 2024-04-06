# import re
# genes = input('Please enter your sequences: ')
# s_cerevisiae = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
# s_cerevisiae_text = s_cerevisiae.read().split('\n')
# def prev_line(text, line):
#     lines = text
#     index = lines.index(line)
#     if index > 0:
#         return lines[index - 1]
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
genes = input('Please enter your sequences: ')
s_cerevisiae = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
s_cerevisiae_text = s_cerevisiae.readlines()
def prev_line(line_number, lines):
    if line_number > 0:
        return lines[line_number - 1].strip() 
    else:
        return None
fasta_file_1 = ''
fasta_file_2 = ''
count1 = 0
count2 = 0
if genes == 'GTGTGT':
    for line_number, line in enumerate(s_cerevisiae_text):
        if 'GTGTGT' in line:
            prev_line_content = prev_line(line_number, s_cerevisiae_text)
            if prev_line_content:
                gene_name1 = re.findall(r'gene:.+?\s', prev_line_content)
                if gene_name1:
                    fasta_file_1 += 'The duplicated ' + ', '.join(gene_name1) + '\n'
                    count1 += 1
    print(count1)
    with open('GTGTGT_duplicate_genes.fa', 'w') as f1:
        f1.write(fasta_file_1)
elif genes == 'GTCTGT':
    for line_number, line in enumerate(s_cerevisiae_text):
        if 'GTCTGT' in line:
            prev_line_content = prev_line(line_number, s_cerevisiae_text)
            if prev_line_content:
                gene_name2 = re.findall(r'gene:.+?\s', prev_line_content)
                if gene_name2:  
                    fasta_file_2 += 'The duplicated ' + ', '.join(gene_name2) + '\n'
                    count2 += 1
    print(count2)
    with open('GTCTGT_duplicate_genes.fa', 'w') as f2:
        f2.write(fasta_file_2)
