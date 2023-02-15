#include <iostream>
#include <cstdlib>
using namespace std;

class Cube{
    protected :
    int s;
    int Area;

    public:
    void getSide(){
        cout << "Please enter side of dice\n";
        cin >> s;
    }

    int areacal(){
        Area = 6*s*s;
        return Area;
    }
};

class Dice{
    protected :
    int random;
    
    public :
    int playDice(){
    srand((unsigned) time(NULL));
    random = (rand() % 6) + 1;
    return random;
    }
    
};

class Display : public Dice, public Cube{
    
    public :
    Display(int Area, int random){
        this->Area = Area;
        this->random = random;
        
        cout << "Area of dice is " << Area << "\n";
        cout << "You got "<< random << " on the Dice!\n";
    }
    
};

int main(){
    Cube c1;
    c1.getSide();
    Dice d1;
    Display s1 = Display(c1.areacal(), d1.playDice());
    return 0;
}