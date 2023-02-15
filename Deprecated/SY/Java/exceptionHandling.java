
public class exceptionHandling{

    public static void main (String[] args) {

        int a = 69;
        int b = 0 ;

        try{
           int x = a/b;
        }
        catch(Exception e){
            System.out.println("Arithmetic Exception ");
            System.out.println(e);
        }
        System.out.println();
        
        int [] arr = new int [69];
        try{
            arr[200] = 5;
        }
        catch(Exception e){
            System.out.println("ArrayIndexOutOfBounds Exception");
            System.out.println(e);
        }
        System.out.println();
        
        try{
            Class.forName("Class Mike_Oxmall");
        }
        catch(Exception e){
            System.out.println("ClassNotFound Exception");
            System.out.println(e);
        }
        System.out.println();
    }
}