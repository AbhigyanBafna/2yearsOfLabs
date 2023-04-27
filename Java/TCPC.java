// Client code for a TCP connection to add two numbers.

import java.io.*;
import java.net.*;
import java.util.Scanner;

class TCPC{
    public static void main(String args[]) throws Exception{
        int n1, n2, sum;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter 1st Number : ");
        n1 = sc.nextInt();
        System.out.print("Enter 2st Number : ");
        n2 = sc.nextInt();

        Socket client = new Socket("localhost", 5678);

        DataOutputStream toServer = new DataOutputStream(client.getOutputStream());
        toServer.writeInt(n1);
        toServer.writeInt(n2);

        DataInputStream fromServer = new DataInputStream(client.getInputStream());
        sum = fromServer.readInt();

        System.out.println("Sum of " +n1+ " + " +n2+ " = " +sum);

        client.close();
    }
}