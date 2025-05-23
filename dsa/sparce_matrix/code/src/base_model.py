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
        file.close # Close the file after use

        
        # Declaring rows, columns variables for parsing

        rows = 0 
        cols = 0
        entries = []

        for list_line in sample_list:
            # Parsing the rows part
            if list_line.startswith('rows='):
                outcome = list_line.split('=')
                if len(outcome) == 3:
                    rows = int(outcome[2])
                else:
                    print('Invalid row format:', list_line)
                    return None

            # Parsing the columns part
            elif list_line.startswith('cols='):
                outcome = list_line.split('=')
                if len(outcome) == 3:
                    cols = int(outcome[2])
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
                outcome.append(new_outcome.strip()) # Adds the last part

                if len(outcome) == 3:
                    try:
                        row_n = int(outcome[0])
                        col_n = int(outcome[1])
                        value_n= int(outcome[2])
                        entries.append((row_n, col_n, value))

                    except:
                        print('Invalid format in entry':, list_line)
                        return None

                else:
                    print('Invalid entry format:', list_line)
                    return None

            else:
                print('Invalid List line format:', list_line)
                return None

        print("Matrix Dimensions: ")
        print("Rows:", rows)
        print("Columns:", cols)
        print("Non-zero Entries:", len(entries))
        
        return {
            'rows': rows,
            'Columns': cols,
            'entries': entries

                }

    except:
        print('Error passing content ....')
        return None

# linking with my sample file
the_file = sparce_matrix('../')
