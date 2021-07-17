#import "matrix.hpp"
#import <iostream>

using namespace std;

Matrix::Matrix(size_t rows, size_t cols) {
    m_vector = vector<double>(rows * cols, 0);
    m_rows = rows;
    m_cols = cols;
}

Matrix::Matrix(const Matrix& other) {
    m_vector = vector<double>(other.m_vector);
    m_rows = other.m_rows;
    m_cols = other.m_cols;
}

void Matrix::print() {
    for(int i = 0; i < this->m_vector.size(); i++) {
        if(i > 0 && i % this->m_cols == 0) {
            cout << endl;
        }
        cout << this->m_vector[i] << " ";
    }
    cout << endl;
}

double Matrix::getValueAt(size_t row, size_t col) {
    // input is 1-indexed so subtract 1 from row and column before looking up the value
    return this->m_vector[this->m_cols * (row - 1) + (col - 1)];
}

void Matrix::setValueAt(double value, size_t row, size_t col) {
    this->m_vector[this->m_cols * (row - 1) + (col - 1)] = value;
}

Matrix Matrix::multiply(double value) {
    Matrix newMatrix(*this);
    for(int i = 0; i < newMatrix.m_vector.size(); i++) {
        newMatrix.m_vector[i] *= value;
    }
    return newMatrix;
}

size_t Matrix::getNoOfRows() {
    return this->m_rows;
}

size_t Matrix::getNoOfCols() {
    return this->m_cols;
}

Matrix Matrix::operator + (const Matrix& rhs) {
    return Matrix(this->m_rows, rhs.m_cols);
}

Matrix Matrix::operator * (const Matrix& rhs) {
    return Matrix(0, 0);
}

bool Matrix::operator == (const Matrix& rhs) {
    // return early if internal vectors are not the same size
    if(this->m_vector.size() != rhs.m_vector.size()) {
        return false;
    }
    for(int i = 0; i < this->m_vector.size(); i++) {
        if(this->m_vector[i] != rhs.m_vector[i]) {
            return false;
        }
    }
    return true;
}
