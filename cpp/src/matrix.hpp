#ifndef MATRIX_HPP
#define MATRIX_HPP

#import <vector>

class Matrix {
    public:
        Matrix(std::size_t, std::size_t);

        Matrix(const Matrix& other); // copy constructor

        double getValueAt(std::size_t row, std::size_t col);

        void setValueAt(double value, std::size_t row, std::size_t col);

        Matrix identity(void);

        Matrix multiply(double value);

        std::size_t getNoOfRows(void);

        std::size_t getNoOfCols(void);

        void print(void);

        Matrix operator + (const Matrix& rhs);

        Matrix operator * (const Matrix& rhs);

        bool operator == (const Matrix& rhs);

    private:
        std::vector<double> m_vector;
        std::size_t m_rows, m_cols;
};

#endif
