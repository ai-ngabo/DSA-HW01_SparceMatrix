#!/usr/bin/python3

class SparseMatrix:
    def __init__(self, sample_file=None, rows=None, cols=None):
        """Initialize matrix from a file or create an empty matrix."""
        self.matrix = {}  # Dictionary to store non-zero values
        if sample_file:
            self.load_matrix_from_file(sample_file)
        else:
            self.rows = rows
            self.cols = cols

    def load_matrix_from_file(self, file_path):
        """Read and parse a sparse matrix from a file."""
        try:
            with open(file_path, 'r') as file:
                for list_line in file:
                    list_line = list_line.strip()
                    if not list_line:
                        continue  # for Ignoring empty lines

                    if list_line.startswith("rows="):
                        self.rows = int(list_line.split("=")[1])
                    elif list_line.startswith("cols="):
                        self.cols = int(list_line.split("=")[1])
                    elif list_line.startswith("(") and list_line.endswith(")"):
                        
                        # Parsing the rows, columns and values
                        new_line = list_line[1:-1]  # to Remove parentheses that appear on the sample files
                        row, col, value = map(int, new_line.split(","))
                        self.matrix[(row, col)] = value
                    else:
                        raise ValueError(f"Invalid format in line: {line}")
        except Exception as e:
            raise ValueError(f"Error parsing Sample input files: {e}")

    def addition(self, other):
        """Returns the sum of two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition.")

        result = SparseMatrix(rows=self.rows, cols=self.cols)
        for key in set(self.matrix.keys()).union(other.matrix.keys()):
            result.matrix[key] = self.matrix.get(key, 0) + other.matrix.get(key, 0)
        return result

    def subtraction(self, other):
        """Returns the difference of two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for subtraction.")

        result = SparseMatrix(rows=self.rows, cols=self.cols)
        for key in set(self.matrix.keys()).union(other.matrix.keys()):
            result.matrix[key] = self.matrix.get(key, 0) - other.matrix.get(key, 0)
        return result

    def multiplication(self, other):
        """Returns the product of two sparse matrices."""
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication.")

        result = SparseMatrix(rows=self.rows, cols=other.cols)
        for (row1, col1), value1 in self.matrix.items():
            for col2 in range(other.cols):
                value2 = other.matrix.get((col1, col2), 0)
                if value2 != 0:
                    result.matrix[(row1, col2)] = result.matrix.get((row1, col2), 0) + (value1 * value2)
        return result
    
    #We have to transpose before multiplication of matrices bcz num of cols in 1st matrix must match num of rows in 2nd matrix
    def transpose(self):
        """Returns the transposed version of a sparse matrix."""
        transposed = SparseMatrix(rows=self.cols, cols=self.rows)
        for (row, col), value in self.matrix.items():
            transposed.matrix[(col, row)] = value
        return transposed

    def display(self):
        """Print stored elements of the sparse matrix."""
        print(f"Sparse Matrix ({self.rows}x{self.cols}):")
        for (row, col), value in self.matrix.items():
            print(f"({row}, {col}) -> {value}")


def save_file(matrix, operation):
    """Saves result to a file."""
    file_name = f"result_{operation}.txt"
    with open(file_name, "w") as f:
        f.write(f"Sparse Matrix (rows:{matrix.rows} & cols:{matrix.cols}):\n")
        for (row, col), value in matrix.matrix.items():
            f.write(f"{row}, {col}, {value}\n")
    print(f"\nOutput saved to {file_name}")

def main_menu():
    """Interactive menu to select sparse matrix operations."""
    matrix1 = SparseMatrix("../../sample_inputs/samplefile1.txt")
    matrix2 = SparseMatrix("../../sample_inputs/samplefile2.txt")

    while True:
        print("\nChoose an operation to perform on th two matrices loaded:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit!")


        option = input("Enter the number of your choice (1-4): ")

        if option == "1":
            answer = matrix1.addition(matrix2)
            sign = "addition"
        elif option == "2":
            answer = matrix1.subtraction(matrix2)
            sign= "subtraction"
        elif option == "3":
            answer = matrix1.multiplication(matrix2.transpose())
            sign = "multiplication"
        elif option == "4":
            print('---------------------------------\nExiting the program! ...')
            return

        else:
            print("\nInvalid choice! Choose correct number!.")
            continue

        answer.display()
        save_file(answer, sign)


if __name__ == "__main__":
    main_menu()
