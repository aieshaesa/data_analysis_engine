import csv

columns_list = []

with open("data.csv", 'r') as read_file:
    reader = csv.reader(read_file)
    
    for row in reader:
        found_none = False
        
        # scan row for "NONE"
        for field in row:
            if field == "NONE":
                found_none = True
                break

        if found_none == False:
            if row not in columns_list:
                columns_list.append(row)

# may not need to rewrite, as 'columns_list' now contains no duplicate rows or rows containing "NONE" at this point.
with open('clean.csv', 'w', newline='') as write_file:
    writer = csv.writer(write_file)
    writer.writerows(columns_list)