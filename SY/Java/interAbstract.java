
import java.util.Scanner;

interface Networks{
    String[] Networks = {"Abhi", "Shia", "Aadi", "Sushi", "OSX"};
    default void getNetworks(){
        for (String element:Networks) {
            System.out.println(element);
        }
    }
    void setNetwork();
}

interface BootMenu{
    void switchOff();
    void reboot();
    void airplaneMode();
}

interface Media{
    void Snapshot();
    void RecVideo();
    void RecVoice();
}

abstract class Phone{
    Scanner sc = new Scanner(System.in);
    abstract void pickCall(String Name);
    abstract void dialCall(String Name);
}

class Samsung extends Phone implements Networks,BootMenu,Media{

    Samsung(){
        System.out.println("Hello user this is your Samsung Device, At your service!");
    }

    @Override
    public void getNetworks() {
        Networks.super.getNetworks();
    }

    @Override
    public void setNetwork(){
        System.out.println("Please enter the correct SSID (Network Name)");
        String Navig = sc.nextLine();
        for(int i = 0;i< Networks.length;i++){
            if(Navig.equals(Networks[i])){
                System.out.println("Connected successfully to " + Networks[i]);
            }
        }
    }

    @Override
    public void switchOff() {
        System.out.println("Goodbye people!");
    }

    @Override
    public void reboot() {
        System.out.println("Will be back in a moment");
        System.out.println("...");
        System.out.println("Hope you didn't miss me very much :)");
    }

    @Override
    public void airplaneMode() {
        System.out.println("Taking off...zoom.");
        System.out.println("You are now disconnected from the world! Have a safe journey");
    }

    @Override
    public void Snapshot() {
        System.out.println("Taking a photo, say cheese!");
    }

    @Override
    public void RecVoice() {
        System.out.println("I now listen to every sound!");
    }

    @Override
    public void RecVideo() {
        System.out.println("I now listen to every sound and record every pixel");
    }

    @Override
    void pickCall(String Name) {
        System.out.println("Connecting you to " + Name);
    }

    @Override
    void dialCall(String Name) {
        System.out.println("Calling " +  Name);
    }
}


public class interAbstract{
    public static void main(String[] args) {
       Samsung s1 = new Samsung();
       s1.dialCall("Aadi");
       s1.pickCall("Shia");
       s1.reboot();
       s1.Snapshot();
       s1.RecVideo();
       s1.getNetworks();
       s1.setNetwork();
       s1.RecVoice();
       s1.airplaneMode();
       s1.switchOff();
    }
}