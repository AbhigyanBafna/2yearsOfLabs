import java.util.*;

public class factFiboQuad {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //Factorial
        System.out.print("Enter a number for its Factorial: ");
        int n = sc.nextInt();
        System.out.println("");
        int fact = 1;
        for (int i = 1; i <= n; i++) {
            fact = fact * i;
        }
        System.out.println("Factorial is " + fact);
        System.out.println("");
        System.out.println("");


        //Fibonacci
        System.out.println("Fibonacci series");
		System.out.print("enter the value of f : ");
		int f = sc.nextInt();
		int n1 = 0;
		int n2 = 1;
		
		for(int i=0;i<f;i++){
		    int temp = n1 + n2;
		    n1 = n2;
		    n2 = temp;
		    temp = n1 ;
		    System.out.println(n1);
		}	
    	System.out.println("");
    	System.out.println("");


        //Quadratic Eqn
        double r1, r2;
        System.out.print("Enter value for a in Eqn : ");
        double a = sc.nextInt();
        System.out.println("");
        System.out.print("Enter value for b in Eqn : ");
        double b = sc.nextInt();
        System.out.println("");
        System.out.print("Enter value for c in Eqn : ");
        double c = sc.nextInt();
        System.out.println("");
        r1 = -b + Math.sqrt((b * b - 4 * a * c))/(2*a);
        r2 = -b - Math.sqrt((b * b - 4 * a * c))/(2*a);
        System.out.println("The algebraic roots of the equation are " + r1 + " and " + r2 + ".");

          }
    }