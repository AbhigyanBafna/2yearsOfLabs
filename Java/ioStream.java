import java.io.*;

class ioStream{
    public static void main(String args[]) throws IOException{
        char c;
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        System.out.print("Enter the character : ");
        c = (char)br.read();
        System.out.println(c);

        FileInputStream in = new FileInputStream("Input.txt");
        FileOutputStream out = new FileOutputStream("Output.txt");
        int a;
        int k = 0;
        while((a = in.read()) != -1){
            out.write(a);
            System.out.print((char)a);
            k++;
        }
        System.out.println();
        System.out.println("No of char copied : " + k);
    }
}