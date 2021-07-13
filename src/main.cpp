#import "matrix.hpp"
#import <iostream>

int main() {
    Matrix m1(2, 2);
    Matrix m2(2, 2);
    m1.print();
    m2.print();

    Matrix m3 = m1 + m2;

    m3.print();

    return 0;
}
