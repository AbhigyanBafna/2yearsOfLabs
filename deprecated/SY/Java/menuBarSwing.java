
import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class menuBarSwing extends JFrame implements ActionListener{
	
	JFrame f;
	JMenuBar mb;
	JMenu file, edit, help;
	JMenuItem cut,copy,paste, selectAll, open, save, newF, close,feedback,exit;
	JTextArea ta;
	
	menuBarSwing(){
	super("NodePad Using GUI");
	f = new JFrame();
	mb = new JMenuBar();
	f.add(mb);
	
	file = new JMenu("File");
	edit = new JMenu("Edit");
	help = new JMenu("Help");
	mb.add(file);
	mb.add(edit);
	mb.add(help);
	
	cut = new JMenuItem("Cut");
	copy = new JMenuItem("Copy");
	paste = new JMenuItem("Paste");
	selectAll = new JMenuItem("Select All");
	
	edit.add(cut);
	edit.add(copy);
	edit.add(paste);
	edit.add(selectAll);
	
	cut.addActionListener(this);
	copy.addActionListener(this);
	paste.addActionListener(this);
	selectAll.addActionListener(this);
	
	open = new JMenuItem("Open File");
	save = new JMenuItem("Save File");
	newF = new JMenuItem("New File");
	close = new JMenuItem("Close File");
	file.add(open);
	file.add(save);
	file.add(newF);
	file.add(close);
	
	feedback = new JMenuItem("Feedback");
	exit = new JMenuItem("Exit");
	help.add(feedback);
	help.add(exit);
	
	ta = new JTextArea();
	ta.setBounds(10,10,580,380);
	f.add(ta);
	
	f.setJMenuBar(mb);
	f.setSize(600,450);
	f.setLayout(null);
	f.setLocation(300,100);
	f.setVisible(true);
}

	public void actionPerformed(ActionEvent e){
	if(e.getSource() == cut){
	ta.cut();
	}
	if(e.getSource() == copy){
	ta.copy();
	}
	if(e.getSource() == paste){
	ta.paste();
	}
	if(e.getSource() == selectAll){
	ta.selectAll();
	}
	}


	public static void main(String args[]){
	new menuBarSwing();
}
}