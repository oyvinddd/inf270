#import "matrix.hpp"
#import <iostream>

Matrix::Matrix(int i, int j) {

    for(std::size_t k = 0; k < i; k++) {
        std::vector<double> temp(j, 0);
        m_vect.push_back(temp);
    }
}

void Matrix::print() {
    for(std::size_t i = 0; i < m_vect.size(); i++) {
        std::vector<double> temp = m_vect[i];
        for(std::size_t j = 0; j < temp.size(); j++) {
            std::cout << temp[j]
        }
    }
}
