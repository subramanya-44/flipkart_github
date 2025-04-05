import csv

with open('flip.csv', 'r', encoding='utf-8') as infile, open('flip_clean.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
    
    for row in reader:
        clean_row = [col.replace('"', '').replace('\n', ' ').replace('\r', ' ') for col in row]
        writer.writerow(clean_row)
