package Study_2022.baekjoon.shim.Java.알고리즘_분류.재귀;

import java.io.*;
import java.util.*;

public class n_11729 {
    public static BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    public static void hanoi(int n, int from, int by, int to)throws IOException{
        if(n==1)
            bw.write(from+" "+to+"\n");
        else{
            hanoi(n-1, from, to, by);
            bw.write(from+" "+to+"\n");
            hanoi(n-1, by, from, to);
        }
    }
    public static void main(String[]args)throws IOException{
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println((int)Math.pow(2, n)-1);
        hanoi(n, 1, 2, 3);
        bw.flush();
        bw.close();
    }
}