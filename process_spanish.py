import unidecode
import string

INPUT_FILE = 'segunda_guerra.txt'

file_content = ""

with open(INPUT_FILE, 'r+') as f:
    file_content = f.read()

unaccented_string = unidecode.unidecode(file_content).lower()

for c in string.punctuation:
    #if c not in '.,#':
    unaccented_string = unaccented_string.replace(c, "")

OUTPUT_FILE = 'PROCESSED_' + INPUT_FILE
with open(OUTPUT_FILE, 'w+') as out:
    out.write(unaccented_string)