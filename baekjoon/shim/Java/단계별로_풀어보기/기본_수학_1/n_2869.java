package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기본_수학_1;

import java.io.*;

public class n_2869 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String[] st=br.readLine().split(" ");
        int A=Integer.parseInt(st[0]);
		int B=Integer.parseInt(st[1]);
		int V=Integer.parseInt(st[2]);
        System.out.println((V-B)/(A-B)+(((V-B)%(A-B))==0?0:1));
    }
}
