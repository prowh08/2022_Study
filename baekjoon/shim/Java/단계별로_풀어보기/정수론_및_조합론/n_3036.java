package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정수론_및_조합론;

import java.io.*;

public class n_3036 {
    public static int gcd(int n, int m){
        if(m==0)
            return n;
        else 
            return gcd(m,n%m);
    }
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int T=Integer.parseInt(br.readLine()), arr[]= new int[T];
        String st[]=br.readLine().split(" ");
        for(int i=0; i<T;i++)
            arr[i]=Integer.parseInt(st[i]);
        for(int i=1; i<T; i++){
            int gcdn=gcd(arr[i],arr[0]);
            bw.write(arr[0]/gcdn+"/"+arr[i]/gcdn+"\n");
        }
        bw.flush();bw.close();
    }
}
