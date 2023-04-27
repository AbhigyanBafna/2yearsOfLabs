// Server code for a TCP connection to add two numbers.

import java.io.*;
import java.net.*;

class TCPS{
    public static void main(String args[]) throws Exception{
        int n1, n2, sum;

        ServerSocket server = new ServerSocket(5678);

        while(true){
            Socket connection = server.accept();

            DataInputStream fromClient = new DataInputStream(connection.getInputStream());
            n1 = fromClient.readInt();
            n2 = fromClient.readInt();

            sum = n1 + n2;
            System.out.println(n1 +" + "+ n2 +" = "+ sum);
            System.out.println("Sending to client");
            
            DataOutputStream toClient = new DataOutputStream(connection.getOutputStream());
            toClient.writeInt(sum);
        }
    }
}