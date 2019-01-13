// The "ReadLib " class by R.Parteno February 2001
// ReadLib is a library class of read routines all based upon pressing the enter key
// ReadLib provides methods for reading int, double, boolean, char and String types

import java.io.*;
import java.util.*;

public class ReadLib
{
    // the Tokenizer is used to get the first item typed on a line, used with
    //  readInt(), readDouble(), and readBoolean()
    static private StringTokenizer stok;
    
    // the BufferedReader opens the connection to the keyboard
    static private BufferedReader br
	= new BufferedReader (new InputStreamReader (System.in));

    public static int readInt ()   // uses a Tokenizer and Integer wrapper class
    {                                //  to get a true int value
	int i;
	try
	{
	    String str = br.readLine ();
	    StringTokenizer stok = new StringTokenizer (str);
	    i = new Integer (stok.nextToken ()).intValue ();
	}
	catch (IOException ex)      // connection failure
	{
	    System.out.println (ex);
	    i = 0;
	}
	catch (NumberFormatException nfe)  // invalid keyboard entry
	{
	    System.out.println ("Warning: A non-numeric value was entered");
	    System.out.println ("Your variable has been given value of 0");
	    i = 0;
	}
	return i;
    }


    public static double readDouble ()// uses a Tokenizer and Double wrapper class
    {                                //  to get a true double value
	double d = 0;
	try
	{
	    String str = br.readLine ();
	    stok = new StringTokenizer (str);
	    d = new Double (stok.nextToken ()).doubleValue ();
	}
	catch (IOException io)
	{
	    System.out.println (io);
	}
	catch (NumberFormatException nfe)
	{
	    System.out.println ("Warning: A non-numeric value was entered");
	    System.out.println ("Your variable has been given value of 0");
	    d = 0;
	}
	return d;
    }


    public static boolean readBoolean ()   // reads a boolean, looks for trus or false
    {                                       // assumes false otherwise
	boolean result = false;

	try
	{
	    String str = br.readLine ();
	    stok = new StringTokenizer (str);
	    String answer = stok.nextToken ();
	    if (answer.equals ("true"))   // valid true entry
	    {
		result = true;
	    }
	    else
	    {
		if (!answer.equals ("false"))  // invalid entry
		    System.out.println ("An invalid value was entered, false ia assumed");
		result = false;
	    }
	}
	catch (IOException io)
	{
		System.out.println (io);
	}

	return result;

    }

    public static char readChar ()
    {
	char oneChar = ' ';

	try
	{

	    String str = br.readLine ();
	    oneChar = str.charAt (0);   // oneChar is first character of keyboard entry 
	}
	catch (IOException io)      // connection error
	{
	    System.out.println (io);
	}
	catch (StringIndexOutOfBoundsException se)  // enter key only, no character 
	{
	    System.out.println ("There was no character entered, blank assumed");
	}
	return oneChar;
    }

    public static String readString ()
    {
	String str="";
	try
	{

	    str = br.readLine ();   // returns null if no characters typed

	}
	catch (IOException io)
	{
	    System.out.println (io);
	}
	
	return str;
    }
} // ReadLib class
