#ifndef MATRIX_HPP
#define MATRIX_HPP

#import <vector>

class Matrix {
    public:
        Matrix(int, int);

        Matrix operator+(const Matrix& m);

        void print();

    private:
        std::vector<std::vector<double> > m_vect;
};

#endif
