import blosum as bl
matrix = bl.BLOSUM(62)
file_path_huamn = r'D:\IBI\IBI1_2023-24\Practical13\SLC6A4_HUMAN.fa'
file_path_mouse = r'D:\IBI\IBI1_2023-24\Practical13\SLC6A4_MOUSE.fa'
file_path_rat = r'D:\IBI\IBI1_2023-24\Practical13\SLC6A4_RAT.fa'

File_Human = open(file_path_huamn)
File_Mouse = open(file_path_mouse)
File_Rat = open(file_path_rat)
Human_sequence = ''
Mouse_sequence = ''
Rat_sequence = ''
for line in File_Human:
    if not line.startswith('>'):
        Human_sequence += line.strip()
for line in File_Mouse :
    if not line.startswith('>'):
        Mouse_sequence += line.strip()
for line in File_Rat:
    if not line.startswith('>'):
        Rat_sequence += line.strip()

identical_count = 0
alignment_score = 0

for i in range(len(Human_sequence)):
    alignment_score += matrix[Human_sequence[i]][Mouse_sequence[i]]
    if Human_sequence[i]== Mouse_sequence[i]:
        identical_count += 1
print ('The identical percentage of human and mouse is' , identical_count/len(Human_sequence) * 100 , '%')
print('The alignment score of human and mouse is ', alignment_score)
identical_count = 0
alignment_score = 0

for i in range(len(Human_sequence)):
    alignment_score += matrix[Human_sequence[i]][Rat_sequence[i]]
    if Human_sequence[i]==Rat_sequence[i]:
        identical_count += 1
print ('The identical percentage of human and rat is' , identical_count/len(Human_sequence) * 100 , '%')
print('The alignment score of human and rat is ', alignment_score)
identical_count = 0
alignment_score = 0

for i in range(len(Mouse_sequence)):
    alignment_score += matrix[Rat_sequence[i]][Mouse_sequence[i]]
    if Mouse_sequence[i]==Rat_sequence[i]:
        identical_count += 1
print ('The identical percentage of rat and mouse is' , identical_count/len(Human_sequence) * 100 , '%')
print('The alignment score of rat and mouse is ', alignment_score)




