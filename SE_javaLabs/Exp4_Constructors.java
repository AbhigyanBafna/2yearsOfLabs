import java.util.*;

public class Main {
    public static void main(String[] args) {
        shape r1 = new shape();
        System.out.print("Square Side : ");
        Scanner sc = new Scanner(System.in);
        double s = sc.nextInt();
        System.out.println("");
        r1.Rectangle();
        r1.Square();
        r1.Triangle();
        r1.Cube(s);
        r1.Sphere();
        r1.Cylinder();
    }
}

class shape {
    double  l,b,h,r;
    double vol,tsa;
    double pi = Math.round((Math.PI*100)/100);
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
        double Area = l*b;
        System.out.println("Area of Rectangle = " + Area);
    }

    void Square(){
        double Area = l*l;
        System.out.println("Area of Square= " + Area);
    }
    void Triangle(){
        double Area = l*b*0.5;
        System.out.println("Area of Triangle= " + Area);
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

    void Cylinder(){
        vol = pi*r*r*h;
        System.out.println("Volume of Cylinder = " + vol);
        tsa = pi*r*r*2 + 2*pi*r*h;
        System.out.println("Total Surface Area = " + tsa + "\n");
    }

}