import javax.swing.*;
import java.awt.event.*;

class Studentform extends JFrame implements ActionListener {

JLabel l1,l2,l3,l4,l5;
JTextField tx1, tx2;
JRadioButton rb1, rb2, rb3;
JComboBox cb;
JCheckBox cb1, cb2, cb3, cb4;
JButton b;
JTextArea area;

@SuppressWarnings("unchecked")
Studentform(){

JFrame f = new JFrame("Student Form");
JLabel l1 = new JLabel("Name :");
l1.setBounds(20, 20, 80, 30);
tx1 = new JTextField();
tx1.setBounds(100, 20 , 150, 30);
f.add(l1);
f.add(tx1);

JLabel l2 = new JLabel("Mobile No. :");
l2.setBounds(20, 70, 80, 30);
tx2 = new JTextField();
tx2.setBounds(100, 70 , 150, 30);
f.add(l2);
f.add(tx2);

JLabel l3 = new JLabel("Gender :");
l3.setBounds(20, 120, 80, 30);
rb1 = new JRadioButton("Male");
rb1.setBounds(100, 120, 60, 30);
rb2 = new JRadioButton("Female");
rb2.setBounds(180, 120, 60, 30);
rb3 = new JRadioButton("Prefer not to say");
rb3.setBounds(260, 120, 60, 30);

ButtonGroup bg = new ButtonGroup();
bg.add(rb1);
bg.add(rb2);
bg.add(rb3);
f.add(rb1);
f.add(rb2);
f.add(rb3);
f.add(l3); 

JLabel l4 = new JLabel ("Age");
l4.setBounds(20, 165, 80, 30);
String age[] = {"18","19","20","21","22"};

cb = new JComboBox(age);
cb.setBounds(100,170,90, 20);
f.add(l4);
f.add(cb);

JLabel l5 = new JLabel ("Hobbies");
l5.setBounds(20, 215, 50, 30);
f.add(l5);
cb1 = new JCheckBox("Reading");
cb1.setBounds(80,220,80, 20);
cb2 = new JCheckBox("Sports");
cb2.setBounds(160,220,80, 20);
cb3 = new JCheckBox("Dancing");
cb3.setBounds(240,220,80, 20);
cb4 = new JCheckBox("Travel");
cb4.setBounds(320,220,80, 20);
f.add(cb1);
f.add(cb2);
f.add(cb3);
f.add(cb4);

JButton b = new JButton("Submit");
b.setBounds(140,280,75, 20);
f.add(b);

area = new JTextArea();
area.setBounds(30,320,320,100);
f.add(area);
b.addActionListener(this); 

setDefaultCloseOperation(EXIT_ON_CLOSE);
f.setLayout(null);
f.setVisible(true);
f.setSize(400, 500);

}

public void actionPerformed (ActionEvent e) {

String name  = tx1.getText();
String mobile  = tx2.getText();
String gender  = rb1.isSelected() ? "Male":rb2.isSelected() ? "Female" :rb3.isSelected() ? "Prefer not to say":"-";

String age = cb.getItemAt(cb.getSelectedIndex()).toString();
String hobby="";

if (cb1.isSelected()){ 
	hobby = "Reading";
}

if (cb2.isSelected()){ 
	hobby += " " + "Sports";
}

if (cb3.isSelected()){ 
	hobby += " " + "Dancing";
}

if (cb4.isSelected()){ 
	hobby += " " + "Travel";
}

area.setText("Name :"+ name + "\n" + "Mobile Number :" + mobile + "\n" + "Gender :" + gender + "\n" + "Age :" + age + "\n" + "Hobbies :" + hobby);

}


	public static void main(String[] args){ 
		new Studentform();
	}
}
