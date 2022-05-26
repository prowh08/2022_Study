package Study_2022.baekjoon.shim.Java.알고리즘_분류.기본_수학_2;

import java.io.*;

public class n_9020 {
    public static boolean is_prime(int n){
        if(n==1) return false;
        for(int i=2; i<=Math.sqrt(n); i++){
            if(n%i==0)
                return false;
        }
        return true;
    }
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int T=Integer.parseInt(br.readLine());
        for(int i=0; i<T; i++){
            int n=Integer.parseInt(br.readLine());
            for(int j=n/2; j>=1; j--){
                if(is_prime(j)&&is_prime(n-j)){
                    bw.write(j+" "+(n-j)+"\n");
                    break;
                }
            }
        } 
        bw.flush();
        bw.close();
    }
}
