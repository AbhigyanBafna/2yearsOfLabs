import java.util.*;

public class arrays{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in); //Scanner for User Input

        System.out.print("Enter No of Rows : ");
        int row = sc.nextInt();
        System.out.print("Enter No of Columns : ");
        int col = sc.nextInt(); //Taking input for matrix

        int matrix[][] = new int[row][col]; //Matrix is a multidimentional array. Which basically means it can store an array inside an array.
        int r = 0;

        for(int i = 0 ; i<row ; i++){
            r++;
            int k = 1;
            for(int j = 0; j < col; j++){
                
                System.out.printf("Enter Row %d Element %d : ",r,k);
                k++;
                matrix[i][j] = sc.nextInt();
            }

        }
        System.out.println("Matrix - ");
        for(int i = 0 ; i<row ; i++){
            for(int j = 0; j < col; j++){
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println("");
        }
    }
}