package Study_2022.baekjoon.shim.Java.알고리즘_분류.기본_수학_1;

import java.io.*;

public class n_10250 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            String st[]=br.readLine().split(" ");
            int n1=Integer.parseInt(st[0]);
            int n2=Integer.parseInt(st[1]);
            int n3=Integer.parseInt(st[2]);
            System.out.println(n3%n1==0?n3*100+n1/n3:n3%n1*100+n3/n1+1);
        }
    }
}
