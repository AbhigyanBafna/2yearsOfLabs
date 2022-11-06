import java.util.*;

public class Overloading {
    public static void main(String[] args) {
        shape r1 = new shape(); 
        shape r2 = new shape(10); //Constructor Overloaded

        r1.Cube();
        System.out.print("\nVariable Side Length : ");
        Scanner sc = new Scanner(System.in);
        double s = sc.nextInt();
        r1.Cube(s); //Cube Method Overloaded

        r2.Sphere();
        double tsa = r2.Sphere(10); //Sphere Method Overloaded
        System.out.println("Total Surface Area = " + tsa+ "\n");
    }
}

class shape {
    double  l,r, vol,tsa;
    Scanner sc = new Scanner(System.in);

    shape(){ //Default constructor
        System.out.println("Please Enter the following : ");
        System.out.print("Side Length : ");
        l = sc.nextInt();
    }

    shape(int rad){ //Parameterized Constructor
        r = rad;
    }

    void Cube(){ //Method without Parameters
        vol = l*l*l;
        System.out.println("Volume of Cube = " + vol);
    }

    void Cube(double s){ //Method with Parameters
        vol = s*s*s;
        System.out.println("Volume of Cube = " + vol +  "\n" );
    }

    void Sphere(){
        vol = (4/3)* 3.14 *r*r*r;
        System.out.println("Volume of Sphere = " + vol);
    }

    double Sphere(int r){
        tsa = 4* 3.14 *r*r;
        return tsa;
    }
}