package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.io.*;

public class n_1932 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int dp[][]=new int[n][];
        for(int i=0; i<n; i++){
            dp[i]=new int[i+1];
            String st[]=br.readLine().split(" ");
            for(int j=0; j<st.length; j++)
                dp[i][j]=Integer.parseInt(st[j]);
        }
        for(int i=n-1; i>=0; i--){
            for(int j=0; j<i; j++)
                dp[i-1][j]+=Math.max(dp[i][j], dp[i][j+1]);
        }
        System.out.println(dp[0][0]);
    }
}
