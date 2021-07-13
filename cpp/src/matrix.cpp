#import "matrix.hpp"
#import <iostream>

Matrix::Matrix(std::size_t rows, std::size_t cols) {
    m_rows = rows;
    m_cols = cols;
    for(std::size_t i = 0; i < rows; i++) {
        std::vector<double> temp(cols, 0);
        m_vect.push_back(temp);
    }
}

void Matrix::print() {
    for(std::size_t i = 0; i < m_vect.size(); i++) {
        std::vector<double> temp = m_vect[i];
        for(std::size_t j = 0; j < temp.size(); j++) {
            std::cout << temp[j];
            std::cout << " ";
        }
        std::cout << "" << std::endl;
    }
}

Matrix Matrix::operator + (const Matrix& rhs) {
    return Matrix(this->m_rows, rhs.m_cols);
}

Matrix Matrix::operator * (const Matrix& rhs) {
    return Matrix(0, 0);
}
