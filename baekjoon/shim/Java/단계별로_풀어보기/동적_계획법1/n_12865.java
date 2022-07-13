package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.io.*;

public class n_12865 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String st[]=br.readLine().split(" ");
        int n1=Integer.parseInt(st[0]), n2=Integer.parseInt(st[1]);
        int arr1[]=new int[n1+1], arr2[]=new int[n1+1], dp[][]=new int[n1+1][n2+1];
        for(int i=1; i<=n1; i++){
            st=br.readLine().split(" ");
            arr1[i]=Integer.parseInt(st[0]);
            arr2[i]=Integer.parseInt(st[1]);
        }
        for(int i=1; i<=n1; i++){
            for(int j=1; j<=n2; j++){
                if(arr1[i]>j)
                    dp[i][j]=dp[i-1][j];
                else
                    dp[i][j]=Math.max(dp[i-1][j],dp[i-1][j-arr1[i]]+arr2[i]);
            }
        }
        System.out.println(dp[n1][n2]);
    }
}
