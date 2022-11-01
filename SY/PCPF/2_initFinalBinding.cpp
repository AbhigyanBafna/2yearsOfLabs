#include <iostream>
using namespace std;

class Car{

   // INITIALIZATION
   Car()//Default constructor
   {}

   // FINALIZATION
   ~Car()  // Destructor
    {}
};

//STATIC BINDING
class fSum{
public:
    int sum(int a, int b){ return a + b;}
    int sum(int a, int b, int c){ return a + b + c;}
};

// DYNAMIC BINDING
class B
{
public:
    // function f() is declared as virtual in the base class
    virtual void f()
    {
        cout << "\nThe base class function is called.\n";
    }
};

class D : public B
{
public:
    void f() //function overriding
    {
        cout << "The derived class function is called.\n";
    }
};

int main()
{
    fSum obj;
    int a = 10, b = 20, c = 30;
    cout << "The sums are " << obj.sum(a, b) << " " << obj.sum(a, b,c); 

    B base;    // base class object
    D derived; //derived class object

    base.f();       //calls function of base class
    derived.f();       //calls function of derived class
}