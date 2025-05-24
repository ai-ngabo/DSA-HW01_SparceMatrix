class SparseMatrix:
    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        """Initialize matrix from a file or create an empty matrix."""
        self.matrix = {}  # Dictionary to store non-zero values
        if file_path:
            self.load_matrix_from_file(file_path)
        else:
            self.num_rows = num_rows
            self.num_cols = num_cols

    def load_matrix_from_file(self, file_path):
        """Read and parse a sparse matrix from a file."""
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue  # Ignore empty lines
                    
                    if line.startswith("rows="):
                        self.num_rows = int(line.split("=")[1])
                    elif line.startswith("cols="):
                        self.num_cols = int(line.split("=")[1])
                    elif line.startswith("(") and line.endswith(")"):
                        # Parse (row, col, value)
                        new_line = line[1:-1]  # Remove parentheses
                        row, col, value = map(int, new_line.split(","))
                        self.set_element(row, col, value)
                    else:
                        raise ValueError(f"Invalid format in line: {line}")
        except Exception as e:
            raise ValueError(f"Error parsing file content: {e}")

    def get_element(self, row, col):
        """Retrieve value at a given position, default to 0 if missing."""
        return self.matrix.get((row, col), 0)

    def set_element(self, row, col, value):
        """Set a value in the matrix, only storing non-zero values."""
        if value != 0:
            self.matrix[(row, col)] = value
        elif (row, col) in self.matrix:
            del self.matrix[(row, col)]  # Remove zero entries to maintain sparsity

    def add(self, other):
        """Returns the sum of two sparse matrices."""
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for addition.")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (row, col), value in self.matrix.items():
            result.set_element(row, col, value + other.get_element(row, col))
        for (row, col), value in other.matrix.items():
            if (row, col) not in self.matrix:
                result.set_element(row, col, value)
        return result

    def subtract(self, other):
        """Returns the difference of two sparse matrices."""
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for subtraction.")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (row, col), value in self.matrix.items():
            result.set_element(row, col, value - other.get_element(row, col))
        for (row, col), value in other.matrix.items():
            if (row, col) not in self.matrix:
                result.set_element(row, col, -value)
        return result

    def multiply(self, other):
        """Returns the product of two sparse matrices."""
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions are incompatible for multiplication.")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for (row1, col1), value1 in self.matrix.items():
            for col2 in range(other.num_cols):
                value2 = other.get_element(col1, col2)
                if value2 != 0:
                    result.set_element(row1, col2, result.get_element(row1, col2) + (value1 * value2))
        return result

    def display(self):
        """Print stored elements of the sparse matrix."""
        print(f"Sparse Matrix ({self.num_rows}x{self.num_cols}):")
        for (row, col), value in self.matrix.items():
            print(f"({row}, {col}) -> {value}")

# Example Usage
A = SparseMatrix("../../sample_inputs/matrixfile3.txt")
B = SparseMatrix("matrixB.txt")

C = A.add(B)        # Addition
D = A.subtract(B)   # Subtraction
E = A.multiply(B)   # Multiplication

C.display()  # Show result
D.display()
E.display()
