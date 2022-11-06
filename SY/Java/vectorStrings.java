import java.util.*;
import java.lang.String;

public class vectorStrings{
    public static void main(String args[]){
        vectors v1 = new vectors();
        strings s1 = new strings();
    }
}

class vectors{
    @SuppressWarnings("unchecked") //For supressing Xlint warnings. Ignore it.
    vectors(){
        Vector v = new Vector(); //Declaration of a vector.
        v.add("Vector");
        v.add("is");
        v.add("implemented");
        v.add("without deletion"); //Adding to a vector
        System.out.println("Output 1 : " + v); // Displaying a vector.
        System.out.println();

        v.remove("without deletion"); //Deleting from a vector
        v.add("with deletion");

        System.out.println("Output 2 : " + v);
        System.out.println("End of vectors \n");
    }
}

class strings{
    strings(){
        String str = "Abhigyan"; 
        char arr[] = {'H','e','l','l','o'}; 
        String str1 = new String(arr); //Converting char array to a string.
        System.out.println(str);
        System.out.println(str1);
        System.out.println("Length : " + str.length());

        int comp = str.compareTo(str1);
        if(comp == 0){
           System.out.println("Strings are equal "); 
        }
        else if(comp > 0){
            System.out.println("str has more characters than str1"); 
        }
        else{
            System.out.println("str has less characters than str1"); 
        }

        System.out.println(str.concat(str1));
        System.out.println(str.substring(0,4)); //Returns first four characters in str.
        System.out.println("End of Strings \n");
    }
}
