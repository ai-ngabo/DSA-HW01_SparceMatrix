#!/usr/bin/python3
def sparce_matrix(sample_file):
# I start by reading the sample files 
    try:
        file = open(sample_file, 'r')
        sample_list = [] # Empty list to hold data from sample file
        while True:
            list_line = file.readline()
            if not  list_line:
                break
            list_line = list_line.strip()
            if list_line != '':
                sample_list.append(list_line)
        file.close() # Close the file after use

        
        # Declaring rows, columns variables for parsing

        rows = 0 
        cols = 0
        matrix = {}

        for list_line in sample_list:
            # Parsing the rows part
            if list_line.startswith('rows='):
                outcome = list_line.split('=')
                if len(outcome) == 2:
                    rows = int(outcome[1])
                else:
                    print('Invalid row format:', list_line)
                    return None

            # Parsing the columns part
            elif list_line.startswith('cols='):
                outcome = list_line.split('=')
                if len(outcome) == 2:
                    cols = int(outcome[1])
                else:
                    print('Invalid column format:', list_line)
                    return None
            # Parsing the remaining parts (rows, cols, values)
            elif list_line.startswith('(') and list_line.endswith(')'):
                new_line = list_line[1:-1] # To remove the parentheses
                outcome = [] # empty list
                new_outcome = ''
                i = 0
                while i < len(new_line):
                    if new_line[i] != ',':
                        new_outcome += new_line[i]

                    else:
                        outcome.append(new_outcome.strip())
                        new_outcome = ''
                    i += 1
                outcome.append(new_outcome.strip()) # Adds the last part

                if len(outcome) == 3:
                    try:
                        row_n = int(outcome[0])
                        col_n = int(outcome[1])
                        value_n= int(outcome[2])
                        matrix[(row_n, col_n)] = value_n

                    except:
                        print('Invalid format in entry:', list_line)
                        return None

                else:
                    print('Invalid entry format:', list_line)
                    return None

            else:
                print('Invalid List line format:', list_line)
                return None
        print("--------------------------") 
        print("Dimensions of a matrix: ")
        print("Rows: ", rows)
        print("Columns: ", cols)
        print("Entries: ", len(matrix))
        print("--------------------------")
        return {
            'rows': rows,
            'columns': cols,
            'matrix': matrix

                }

    except Exception as e:
        print('Error passing content ....')
        print('Reason:', e)
        return None

# linking with my sample file
the_file = sparce_matrix('../../sample_inputs/matrixfile3.txt')
print(the_file)

class MatrixGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {} 

    def getElement(seld, row, col):
        return self.data.get((row, col), 0)

    def setElement(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value

        elif (row, col) in self.data:
            del self.data[(r, c)]

    def Addition(self, num):
        if self.tows != num.rows or self.cols != num.cols:
            raise ValueError('Dimensions are not matching ....')

        total = MatrixGenerator(self.rows, self.cols)

        for i in 
