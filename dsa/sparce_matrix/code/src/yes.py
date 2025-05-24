#!/usr/bin/python3

def sparse_matrix(sample_file):
    """Reads a sparse matrix from a file and stores non-zero values efficiently."""
    try:
        with open(sample_file, 'r') as file:
            sample_list = [line.strip() for line in file if line.strip()]  # Read and clean data
        
        rows = 0
        cols = 0
        matrix = {}

        for list_line in sample_list:
            if list_line.startswith('rows='):
                outcome = list_line.split('=')
                if len(outcome) == 2:
                    rows = int(outcome[1])
                else:
                    print('Invalid row format:', list_line)
                    return None

            elif list_line.startswith('cols='):
                outcome = list_line.split('=')
                if len(outcome) == 2:
                    cols = int(outcome[1])
                else:
                    print('Invalid column format:', list_line)
                    return None

            elif list_line.startswith('(') and list_line.endswith(')'):
                new_line = list_line[1:-1]  # Remove parentheses
                try:
                    row_n, col_n, value_n = map(int, new_line.split(','))
                    matrix[(row_n, col_n)] = value_n
                except ValueError:
                    print('Invalid format in entry:', list_line)
                    return None
            else:
                print('Invalid line format:', list_line)
                return None

        print("--------------------------")
        print(f"Matrix from {sample_file}:")
        print("Rows:", rows)
        print("Columns:", cols)
        print("Entries:", len(matrix))
        print("--------------------------")

        return {'rows': rows, 'columns': cols, 'matrix': matrix}

    except Exception as e:
        print(f"Error parsing file {sample_file}: {e}")
        return None

# Function to load two files
def load_two_matrices(file1, file2):
    """Loads two sparse matrices from different files."""
    matrix1 = sparse_matrix(file1)
    matrix2 = sparse_matrix(file2)

    if matrix1 and matrix2:
        return matrix1, matrix2
    else:
        print("Error loading one or both files.")
        return None, None

# Example usage with two files
file_path_1 = "../../sample_inputs/samplefile1.txt"
file_path_2 = "../../sample_inputs/samplefile2.txt"

matrix1, matrix2 = load_two_matrices(file_path_1, file_path_2)

def add_matrices(matrix1, matrix2):
    """Adds two sparse matrices and returns the result."""
    if matrix1['rows'] != matrix2['rows'] or matrix1['columns'] != matrix2['columns']:
        raise ValueError("Matrix dimensions do not match for addition.")

    result_matrix = {}

    # Add elements from both matrices
    for key in set(matrix1['matrix'].keys()).union(matrix2['matrix'].keys()):
        result_matrix[key] = matrix1['matrix'].get(key, 0) + matrix2['matrix'].get(key, 0)

    return {'rows': matrix1['rows'], 'columns': matrix1['columns'], 'matrix': result_matrix}

def subtract_matrices(matrix1, matrix2):
    """Subtracts matrix2 from matrix1 and returns the result."""
    if matrix1['rows'] != matrix2['rows'] or matrix1['columns'] != matrix2['columns']:
        raise ValueError("Matrix dimensions do not match for subtraction.")

    result_matrix = {}

    for key in set(matrix1['matrix'].keys()).union(matrix2['matrix'].keys()):
        result_matrix[key] = matrix1['matrix'].get(key, 0) - matrix2['matrix'].get(key, 0)

    return {'rows': matrix1['rows'], 'columns': matrix1['columns'], 'matrix': result_matrix}

def multiply_matrices(matrix1, matrix2):
    """Multiplies two sparse matrices and returns the result."""
    if matrix1['columns'] != matrix2['rows']:
        raise ValueError("Matrix dimensions do not match for multiplication.")

    result_matrix = {}

    # Perform matrix multiplication
    for (row1, col1), value1 in matrix1['matrix'].items():
        for col2 in range(matrix2['columns']):
            value2 = matrix2['matrix'].get((col1, col2), 0)
            if value2 != 0:
                result_matrix[(row1, col2)] = result_matrix.get((row1, col2), 0) + (value1 * value2)

    return {'rows': matrix1['rows'], 'columns': matrix2['columns'], 'matrix': result_matrix}

def transpose_matrix(matrix):
    """Returns the transposed version of a sparse matrix."""
    transposed = {'rows': matrix['columns'], 'columns': matrix['rows'], 'matrix': {}}
    for (row, col), value in matrix['matrix'].items():
        transposed['matrix'][(col, row)] = value
    return transposed



added_matrix = add_matrices(matrix1, matrix2)
subtracted_matrix = subtract_matrices(matrix1, matrix2)
multiplied_matrix = multiply_matrices(matrix1, transpose_matrix(matrix2))

print("Addition Result:", added_matrix)
print("Subtraction Result:", subtracted_matrix)
print("Multiplication Result:", multiplied_matrix)

