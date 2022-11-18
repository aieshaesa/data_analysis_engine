#code to add to main file

""""
def median(number_list):
    sorted_list = sorted(number_list)
    length = len(number_list)
    index = (length - 1)

    if(length % 2):
        result = sorted_list[index]
    else:
        result = (sorted_list[index] + sorted_list[index + 1]) / 2.0

    return result

def main():
    numbers = [4, 5, 8, 9, 10, 17]
"""
import csv

#open csv file
class Airport:
    columns_as_lists = []
    column = []
    size = []

    def __init__(self, filename):
        lines = []
        missing = 'NONE'

        with open(filename, 'r') as read_file:
            reader = csv.reader(read_file)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == missing:
                        lines.remove(row)

        # for loop to ensure no duplicates are added
        no_dup = []
        for i in lines:
            if i not in no_dup:
                no_dup.append(i)

        with open('No_Missing_Values.csv', 'w', newline='') as write_file:
            writer = csv.writer(write_file)
            writer.writerows(no_dup)

        self.load_lists('No_Missing_Values.csv')

    def load_lists(self, file):
        with open(file) as csv_file:
            # creating an object of csv reader
            # with the delimiter
            csv_reader = csv.reader(csv_file, delimiter = ',')
        
            # loop to iterate through the rows of csv
            for row in csv_reader:
        
                # adding first row
                self.column.append(row)
        
                # breaking the loop after the
                # first iteration itself
                break
        csv_file.close()
        with open(file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter = ',')
                
                # number of columns
                self.size = int(len(self.column[0]))
                reader = csv.reader(csv_file)
                # stores each column into array
                self.columns_as_lists = [list(c) for c in zip(*reader)]
                
        # print total number of columns
        """
        print("Total columns:", self.size)

        for i in range(self.size):
            print(i,":", self.columns_as_lists[i][0])
        print("\n")
        """
    
    def drop_column(self, column):
        drop = int(column)
        self.columns_as_lists.pop(drop-1)
        self.size = len(self.columns_as_lists)
        #rows = int(len(self.columns_as_lists[0]))
        #print("size of rows: ", rows)
        #print("new size is: ", self.size)
        



file = 'Airline_Delays_500_Lines.csv'
info = Airport(file) 

active = True

while(active):
    i = 0
    valid = False
    num = 1
    for i in range(info.size):
        print(i+1,":", info.columns_as_lists[i][0])
    print("\n")

    ans = input('Would you like to drop any columns? (y/n) ')

    if ans == 'y' or input == 'Y' or input == 'Yes':
        while(valid == False):
            ans = input('Enter the number of the column you\'d like to drop: ')
            if int(ans) < 1 or int(ans) > info.size:
                print('Name given isn\'t valid, please try again')
            else:
                info.drop_column(ans)
                valid = True
    for i in range(info.size):
        print(i+1,":", info.columns_as_lists[i][0])
    print("\n")

    active = False


"""
    num = 1
    for value in info.column:
        print(num, ' - ', info.column[num-1])
        num += 1

for i in range(info.size):
    # print each column
    print(info.columns_as_lists[i])  # All the values in the first column of your CSV
"""
