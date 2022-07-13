package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.io.*;
import java.util.Arrays;

public class n_9251 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] st1=br.readLine().split(""), st2=br.readLine().split("");
        int dp[][]=new int[st1.length+1][st2.length+1];
        for(int i=0; i<=st1.length; i++)
            Arrays.fill(dp[i], 0);
        for(int i=1; i<=st1.length; i++){
            for(int j=1; j<=st2.length;j++){
                if(st1[i-1].equals(st2[j-1]))
                    dp[i][j]=dp[i-1][j-1]+1;
                else
                    dp[i][j]=Math.max(dp[i][j-1],dp[i-1][j]);
            }
        }
        System.out.println(dp[st1.length][st2.length]);
    }
}