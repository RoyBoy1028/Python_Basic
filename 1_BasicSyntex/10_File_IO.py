import csv

txt_file = open("save.txt", 'w', newline='')
temp = '''
  ___ ___  .__  
 /   |   \ |__| 
/    ~    \|  | 
\    Y    /|  | 
 \___|_  / |__| 
       \/       
                
       '''
txt_file.write(temp)

txt_file.close()

with open("save.txt", 'r', newline='') as txt_file:
    reader = csv.reader(txt_file, delimiter='\n')
    for row in reader:
        print(row)
    
txt_file.close