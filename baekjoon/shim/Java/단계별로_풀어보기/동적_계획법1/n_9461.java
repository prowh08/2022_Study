package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.io.*;

public class n_9461 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int T=Integer.parseInt(br.readLine());
        long arr[]=new long[101];
        arr[1]=arr[2]=arr[3]=1;
        arr[4]=arr[5]=2;
        for(int i=5; i<=100; i++)
            arr[i]=arr[i-1]+arr[i-5];
        for(int i=0; i<T; i++){
            int n=Integer.parseInt(br.readLine());
            bw.write(arr[n]+"\n");
        }
        bw.flush(); bw.close();
    }
}
