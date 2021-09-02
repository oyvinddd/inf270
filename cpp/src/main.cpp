#import "matrix.hpp"
#import <iostream>

void Increment(int& val) {
    val++;
}

int main() {
    Matrix m1(2, 2);
    Matrix m2(2, 2);
    Matrix m3(3, 5);

    m3.setValueAt(10, 2, 3);
    m3.print();

    Matrix m4 = Matrix(m3);//m3.multiply(2);
    m4.setValueAt(30, 1, 1);
    m4.print();
    m3.print();

    Matrix m5 = m4.identity();

    bool isSame = m3 == m4;

    std::cout << isSame << std::endl;
    m5.print();

    int a = 10;
    Increment(a);
    printf("%d", a);

    Increment(a);

    return 0;
}
