// Decompiled by Jad v1.5.8e. Copyright 2001 Pavel Kouznetsov.
// Jad home page: http://www.geocities.com/kpdus/jad.html
// Decompiler options: packimports(3) 
// Source File Name:   2.java

import java.io.*;
import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;

class Exp
{

    Exp()
    {
    }

    public static byte[] decode(byte abyte0[], String s)
        throws Exception
    {
        SecretKeyFactory secretkeyfactory = SecretKeyFactory.getInstance("DES");
        byte abyte1[] = s.getBytes();
        DESKeySpec deskeyspec = new DESKeySpec(abyte1);
        javax.crypto.SecretKey secretkey = secretkeyfactory.generateSecret(deskeyspec);
        Cipher cipher = Cipher.getInstance("DES");
        cipher.init(2, secretkey);
        byte abyte2[] = cipher.doFinal(abyte0);
        return abyte2;
    }

    public static byte[] encode(byte abyte0[], String s)
        throws Exception
    {
        SecretKeyFactory secretkeyfactory = SecretKeyFactory.getInstance("DES");
        byte abyte1[] = s.getBytes();
        DESKeySpec deskeyspec = new DESKeySpec(abyte1);
        javax.crypto.SecretKey secretkey = secretkeyfactory.generateSecret(deskeyspec);
        Cipher cipher = Cipher.getInstance("DES");
        cipher.init(1, secretkey);
        byte abyte2[] = cipher.doFinal(abyte0);
        return abyte2;
    }

    public static void main(String args[])
        throws Exception
    {
        // System.out.println("No");
        // String s = "matreha!";
        // byte abyte0[] = encode("lettreha".getBytes(), s);
        // byte abyte1[] = {
        //     76, -99, 37, 75, -68, 10, -52, 10, -5, 9, 
        //     92, 1, 99, -94, 105, -18
        // };
        // byte name[] = decode(abyte1, s);
        // System.out.println(new String(name));
        // for(int i = 0; i < abyte1.length; i++)
        //     if(abyte1[i] != abyte0[i])
        //     {
        //         System.out.println(abyte1[i] + "--------" + abyte0[i]);
        //         return;
        //     }
        // System.out.println("haha");

        File file = new File("data.bin");
        FileInputStream fileinputstream = new FileInputStream(file);
        byte abyte2[] = new byte[(int)file.length()];
        fileinputstream.read(abyte2);
        fileinputstream.close();
        byte abyte3[] = decode(abyte2, "lettreha");
        FileOutputStream fileoutputstream = new FileOutputStream("stage2.bin");
        fileoutputstream.write(abyte3, 0, abyte3.length);
        fileoutputstream.flush();
        fileoutputstream.close();
    }
}
