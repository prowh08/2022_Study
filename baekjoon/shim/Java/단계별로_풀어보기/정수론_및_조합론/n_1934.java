package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정수론_및_조합론;

import java.io.*;

public class n_1934 {
    public static int gcd(int n, int m){
        if(m==0)
            return n;
        else
            return gcd(m,n%m);
    }
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int T=Integer.parseInt(br.readLine());
        for(int i=0; i<T; i++){
            String st[]=br.readLine().split(" ");
            int n=Integer.parseInt(st[0]),m=Integer.parseInt(st[1]), gcd=gcd(n,m);
            bw.write(n*m/gcd+"\n");
        }
        bw.flush();bw.close();
    }
}
