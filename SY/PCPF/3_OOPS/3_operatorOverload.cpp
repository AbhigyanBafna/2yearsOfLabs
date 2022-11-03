#include <iostream>
#include<math.h>
using namespace std;

class Complex {
private:
float real,imag;
public:
Complex(int r = 0, int i = 0 ) {real = r; imag = i;}

Complex operator + (Complex const &obj) {
Complex res;
res.real = real + obj.real;
res.imag = imag + obj.imag;
return res;
}

Complex operator - (Complex const &obj) {
Complex res;
res.real = real - obj.real;
res.imag = imag - obj.imag;
return res;
}

Complex operator * (Complex const &obj) {
Complex res;
res.real = (real * obj.real) - (imag * obj.imag);
res.imag = (real * obj.imag) + (imag * obj.real);
return res;
}

Complex operator / (Complex const &obj) {
Complex res;
res.real =( (real * obj.real) - (imag * (-obj.imag))) /((obj.real*obj.real)+(obj.imag * obj.imag));
res.imag = ((real * (-obj.imag)) + (imag * obj.real))/((obj.real*obj.real)+(obj.imag * obj.imag));
return res;

}

void print() { cout << real << " + i" << imag << '\n'; }
};

int main()
{
Complex c1(10, 5), c2(2, 4);
Complex add = c1 + c2;
Complex susbs = c1 - c2;
Complex multi = c1 * c2;
Complex divi = c1 / c2;

add.print();
susbs.print();
multi.print();
divi.print();
}