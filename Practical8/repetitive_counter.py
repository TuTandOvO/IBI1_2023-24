seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA' # A DNA sequence
counter_1 = 0
counter_2 = 0
for i in range(0, len(seq)-1):
    substring = seq[i:i+6]  
    if substring == 'GTGTGT':
        counter_1 += 1    
    if substring == 'GTCTGT':
        counter_2 += 1
print(counter_1) # The number of 'GTGTGT' is 1
print(counter_2) # The number pf 'GTCTGT' is 1