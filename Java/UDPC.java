// Client code for a UDP connection to turn a string into uppercase.

import java.io.*;
import java.net.*;
import java.util.Scanner;

class UDPC{
    public static void main(String args[]) throws Exception{
        String s1, ans;

        DatagramSocket client = new DatagramSocket();
        InetAddress IP = InetAddress.getByName("localhost");

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        s1 = sc.nextLine();

        byte[] sendData = new byte[1024];
        byte[] receiveData = new byte[1024];
        sendData = s1.getBytes();

        DatagramPacket toServer = new DatagramPacket(sendData, sendData.length, IP, 3456);
        client.send(toServer);

        DatagramPacket fromServer = new DatagramPacket(receiveData, receiveData.length);
        client.receive(fromServer);

        ans = new String (fromServer.getData());

        System.out.println("String in Uppercase : " + ans);

        client.close();
    }
}