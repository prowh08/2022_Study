package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.io.*;

public class n_2579 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[n+1], dp[]=new int[n+1];
        for(int i=1; i<=n; i++)
            arr[i]=Integer.parseInt(br.readLine());
        dp[1]=arr[1];
        if(n>1)
            dp[2]=arr[1]+arr[2];
        for(int i=3; i<=n; i++)
            dp[i]=Math.max(dp[i-3]+arr[i-1],dp[i-2])+arr[i];
        System.out.println(dp[n]);
    }
}