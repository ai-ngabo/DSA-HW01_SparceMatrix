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
            # Parsing the rows
            if list_line.startswith('rows='):
                outcome = list_line.split('=')
                if len(outcome) == 3:
                    rows = int(outcome[2])
                else:
                    print('Invalid row format:', list_line)
                    return None

            # Parsing the columns
            elif list_line.startswith('cols='):
                outcome = list_line.split('=')
                if len(outcome) == 3:
                    cols = int(outcome[2])
                else:
                    print('Invalid column format:', list_line)
                    return None

