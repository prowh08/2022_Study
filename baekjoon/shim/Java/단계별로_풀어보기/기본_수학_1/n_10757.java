package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기본_수학_1;

import java.io.*;
import java.math.BigInteger;

public class n_10757 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] st=br.readLine().split(" ");
        BigInteger n1=new BigInteger(st[0]), n2=new BigInteger(st[1]);
        System.out.println(n1.add(n2));
    }
}
