package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기본_수학_1;

import java.io.*;

public class n_2775 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(br.readLine());
        for(int i=0; i<T; i++){
            int f=Integer.parseInt(br.readLine()), d=Integer.parseInt(br.readLine());
            int arr[][]=new int[f+1][d+1];
            for (int j=0; j<=f; j++){
                arr[j][1]=1;
                for(int k=1; k<=d; k++){
                    if(j==0) arr[j][k]=k;
                    else arr[j][k]=arr[j][k-1]+arr[j-1][k];
                }
            }
            System.out.println(arr[f][d]);
        }
    }
}
