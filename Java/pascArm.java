import java.util.*;

class pascArmCore{
    Scanner sc = new Scanner(System.in);

    void pasc(){
        
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

    void arm(){

        //Armstrong Number
        System.out.print("Enter a number to check for Armstrong: ");
        int arm = sc.nextInt();
        System.out.println("");
		int rem, sum = 0 , flag = arm;

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
    }
}

public class pascArm {
    public static void main(String[] args) {
      
      pascArmCore s1 = new pascArmCore();
      s1.pasc();
      s1.arm();  
    }
}