import string

hp_content = ''

with open('hp.txt', 'r',encoding='utf8') as hp:
    for line in hp.readlines():
        line = line.lstrip().rstrip()
        if line.isupper():
            line = line + "."
        hp_content += line + '#NEWLINE#'#  + "\n"

#with open('hp.txt', 'r+',encoding='utf8') as hp:
#    hp_content = hp.read()

print(len(hp_content))

for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
    initial = " " + c + "."
    hp_content = hp_content.replace(initial, c)

hp_content = hp_content.replace('Sr.', 'Sr').replace('SR.', 'SR').replace('Mr.', 'Mr').replace('Mrs.', 'Mrs')
hp_content = hp_content.replace('MR.', 'MR').replace('MRS.', 'MRS').replace('mr.', 'mr').replace('mrs.', 'mrs')

hp_content = hp_content.replace("”", "").replace("“", "").replace("’", "").replace(" — ", " ")

for c in string.punctuation:
    if c not in '.,#':
        hp_content = hp_content.replace(c, "")

with open("hp_processed_temp.txt", "w+", encoding='utf8') as out:
    out.write(hp_content)

print(len(hp_content))

hp_content = hp_content.replace('+','').replace("”“", "”. “").replace("” “", "”. “").replace(" — ", " ")
hp_content = hp_content.replace('...', '<suspense>').replace('. . .', '<suspense>').replace(' -','').replace('-','')

#print(len(hp_content))

#hp_content_array = list(hp_content)

#for i in range(0,len(hp_content)):
#    if i%1000==0:
#        print("{}/{}".format(i, len(hp_content)))
#    if hp_content[i]=="“":
#        j = i+1
#        while not hp_content[j]=="”":
#            if hp_content[j]==".":
                #hp_content_array[j]="^"
#                hp_content_array[j]=". "
#            j += 1
#        i = j

#hp_content = ''

#for c in hp_content_array:
#    hp_content += c



hp_array = hp_content.replace('.#NEWLINE#', '.#PARAGRAPH#')
print("1 >>", hp_array[10])

#print(hp_array[0:10])

with open("hp_processed.txt", "w+", encoding='utf8') as out:
    for l in hp_array.split('#PARAGRAPH#'):
        l = l.rstrip().lstrip()
        if l != '':
            l = l.lower().translate(string.punctuation).replace('#newline#',' ')
            #l = l.replace('<suspense>','...').replace('^','.').replace("”", "\"").replace("“", "\"").replace("’", "'")
            l = l.replace('<suspense>','').replace('^','').replace("”", "").replace("“", "").replace("’", "")
            out.write(l + '\n')