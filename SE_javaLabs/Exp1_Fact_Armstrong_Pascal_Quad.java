import java.util.*;

public class Exp1_Fact_Armstrong_Pascal_Quad {
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
      
      
        //Armstrong
        System.out.print("Enter a number to check for Armstrong: ");
        int arm = sc.nextInt();
        System.out.println("");
		    int rem, sum = 0 , flag = n;
		    while (arm>0) {
    			rem = arm%10;
    			sum = sum + (rem*rem*rem);
    			arm=arm/10;
    		}
    		if (sum==flag){
      			System.out.println(flag + " is an Armstrong number");
      		}
    		else{
    			System.out.println(flag + " is not an Armstrong number");
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
        
        
        //Pascals Triangle
        int na, i, j;
        System.out.println("Enter a number of rows: ");
        na = sc.nextInt();
              for (i = 0; i < na; i++) {
                  for (j = 0; j < na - i; j++) {
                      System.out.print("  ");
                  }
                  for (j = 0; j <= i; j++) {
                      System.out.print(fact(i) / (fact(i - j) * fact(j)) + "   ");
                  }
                  System.out.print("\n");
              }
          }
          static int fact(int na) {
              if (na == 0) {
                  return 1;
              }
              return na * fact(na - 1);
          }
    }
