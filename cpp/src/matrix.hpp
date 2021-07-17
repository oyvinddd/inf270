#ifndef MATRIX_HPP
#define MATRIX_HPP

#import <vector>

class Matrix {
    public:
        std::size_t m_rows, m_cols;
        Matrix(std::size_t, std::size_t);

        double value_at(std::size_t row, std::size_t col);
        void print();

        Matrix operator + (const Matrix& rhs);
        Matrix operator * (const Matrix& rhs);
        bool operator == (const Matrix& rhs);

    private:
        std::vector<double> m_vector;
};

#endif
