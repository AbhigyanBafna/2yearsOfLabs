import java.util.*;

public class Overloading {
    public static void main(String[] args) {
        shape r1 = new shape();
        r1.Rectangle();
        r1.Triangle();
        r1.Cube();
        System.out.print("\nVariable Side of Cube : ");
        Scanner sc = new Scanner(System.in);
        double s = sc.nextInt();
        r1.Cube(s);
        r1.Sphere();
    }
}

class shape {
    double  l,b,h,r;
    double vol,tsa, area;
    double pi = 3.14;
    Scanner sc = new Scanner(System.in);

    shape(){
        System.out.println("Please Enter the following : ");
        System.out.print("Length : ");
        l = sc.nextInt();
        System.out.print("Breath : ");
        b = sc.nextInt();
        System.out.print("Height : ");
        h = sc.nextInt();
        System.out.print("Radius : ");
        r = sc.nextInt();
    }

    void Rectangle(){
        area = l*b;
        System.out.println("Area of Rectangle = " + area);
    }

    void Triangle(){
        area = l*b*0.5;
        System.out.println("Area of Triangle= " + area);
    }

    void Cube(){
        vol = l*l*l;
        System.out.println("Volume of Cube = " + vol);
    }

    void Cube(double s){
        vol = s*s*s;
        System.out.println("Volume of Cube = " + vol );
        tsa = 6*s*s;
        System.out.println("Total Surface Area = " + tsa + "\n");
    }

    void Sphere(){
        vol = 4/3*pi*r*r*r;
        System.out.println("Volume of Sphere = " + vol);
        tsa = 4*pi*r*r;
        System.out.println("Total Surface Area = " + tsa+ "\n");
    }
}