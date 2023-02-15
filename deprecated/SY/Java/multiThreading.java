
class Mthread1 implements Runnable{
    @Override
    public void run(){
        for(int i=1;i<=100; i++){
            System.out.println("Marvel");
        }
    }
}

class Mthread2 implements Runnable{
    @Override
    public void run(){
        for(int i=1;i<=5;i++){
            System.out.println("DC");
        }
    }
}

class Mthread3 extends Thread{
    @Override
    public void run(){
        for(int i=1;i<=5;i++){
            System.out.println("Harry Potter");
        }
    }
}

class Mthread4 extends Thread{
    @Override
    public void run(){
        for(int i=1;i<=2;i++){
            System.out.println("Percy Jackson");
        }
    }
}

public class multiThreading{
	public static void main(String[] args) {
		Mthread1 r1 = new Mthread1();
		Thread t1 = new Thread(r1);
		Mthread2 r2 = new Mthread2();
		Thread t2 = new Thread(r2);

        Mthread3 t3 = new Mthread3();
		Mthread4 t4 = new Mthread4();
    
        t2.start();
        t3.start();
        t1.start();
		t4.start();
	}
}


