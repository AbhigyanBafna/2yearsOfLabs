class square{
    
    void area(int side){
        System.out.println("Area is : " + side*side);
    }

    void peri(int side){
        System.out.println("Perimeter is : " + 4*side);
    }
}

class cube extends square{

    void vol(int side){
        System.out.println("Volume is : " + side*side*side);
    }

    void tsa(int side){
        System.out.println("Total Surface Area is : " + 6*side*side);
    }
}

public class inheritance{
	public static void main(String[] args) {
	    cube c1 = new cube();

        c1.area(10);
        c1.peri(10);
        c1.vol(10);
        c1.tsa(10);
	}
}