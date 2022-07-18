package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.누적_합;

import java.io.*;

public class n_11660 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        String st[]=br.readLine().split(" ");
        int n=Integer.parseInt(st[0]),arr[][]=new int[n+1][n+1], dp[][]=new int[n+1][n+1];
        for(int i=0; i<n; i++){
            String str[]=br.readLine().split(" ");
            for(int j=0; j<n; j++){
                arr[i+1][j+1]=Integer.parseInt(str[j]);
                dp[i+1][j+1]=dp[i+1][j]+dp[i][j+1]-dp[i][j]+arr[i+1][j+1];
            }
        }
        for(int i=0; i<Integer.parseInt(st[1]); i++){
            String str[]=br.readLine().split(" ");
            int arr2[]=new int[4];
            for(int j=0; j<4; j++)
                arr2[j]=Integer.parseInt(str[j]);
            bw.write(dp[arr2[2]][arr2[3]]-dp[arr2[2]][arr2[1]-1]-dp[arr2[0]-1][arr2[3]]+dp[arr2[0]-1][arr2[1]-1]+"\n");
        }
        bw.flush();bw.close();
    }
}
