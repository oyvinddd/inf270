#ifndef MATRIX_HPP
#define MATRIX_HPP

#import <vector>

class Matrix {
    public:
        std::size_t m_rows, m_cols;
        Matrix(std::size_t, std::size_t);

        void print();

        Matrix operator + (const Matrix& rhs);
        Matrix operator * (const Matrix& rhs);

    private:
        std::vector<std::vector<double> > m_vect;
};

#endif
