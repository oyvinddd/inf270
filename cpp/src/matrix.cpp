#import "matrix.hpp"
#import <iostream>

Matrix::Matrix(std::size_t rows, std::size_t cols) {
    m_vector = std::vector<double>(rows * cols, 0);
    m_rows = rows;
    m_cols = cols;
}

void Matrix::print() {
    for(int i = 0; i < this->m_vector.size(); i++) {
        if(i > 0 && i % this->m_cols == 0) {
            std::cout << std::endl;
        }
        std::cout << this->m_vector[i] << " ";
    }
    std::cout << std::endl;
}

double Matrix::value_at(std::size_t row, std::size_t col) {
    // input is 1-indexed so subtract 1 from row and column before looking up the value
    return this->m_vector[this->m_cols * (row - 1) + (col - 1)];
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
