// Server code for a UDP connection to turn a string into uppercase.

import java.io.*;
import java.net.*;

class UDPS{
    public static void main(String args[]) throws Exception{
        String normal, uCase;

        DatagramSocket server = new DatagramSocket(3456);

        byte[] receiveData = new byte[1024];
        byte[] sendData = new byte[1024];

        while(true){

            DatagramPacket fromClient = new DatagramPacket(receiveData, receiveData.length);
            server.receive(fromClient);

            normal = new String(fromClient.getData());
            uCase = normal.toUpperCase();
            System.out.println("Recieved String : " + normal);
            System.out.println("Modified String : " + uCase);
            sendData = uCase.getBytes();

            InetAddress IP = fromClient.getAddress();
            int port = fromClient.getPort();

            DatagramPacket toClient = new DatagramPacket(sendData, sendData.length, IP, port);
            server.send(toClient);

        }
    }
}