import os
file_list = [f for f in os.listdir() if f.startswith('Sav')]
with open('backup_file.txt', 'w') as f:
    for file in file_list:
        f.write(file + '\n')
