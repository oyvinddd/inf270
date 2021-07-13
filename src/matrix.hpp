#ifndef MATRIX_HPP
#define MATRIX_HPP

#import <vector>

class Matrix {
    public:
        Matrix();
        Matrix(int, int);
        void print();

    private:
        std::vector<std::vector<double> > m_vect;
};

#endif
