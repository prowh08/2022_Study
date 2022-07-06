package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.io.*;

public class n_1149 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(br.readLine());
        int dp[][]=new int[T][3];
        String str[]=br.readLine().split(" ");
        for(int i=0; i<3; i++)
            dp[0][i]=Integer.parseInt(str[i]);
        for(int i=1; i<T; i++){
            String st[]=br.readLine().split(" ");
            dp[i][0]=Math.min(dp[i-1][1],dp[i-1][2])+Integer.parseInt(st[0]);
            dp[i][1]=Math.min(dp[i-1][0],dp[i-1][2])+Integer.parseInt(st[1]);
            dp[i][2]=Math.min(dp[i-1][0],dp[i-1][1])+Integer.parseInt(st[2]);
        }
        System.out.println(Math.min(dp[T-1][0],Math.min(dp[T-1][1],dp[T-1][2])));
    }
}
