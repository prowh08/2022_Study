package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.io.*;
import java.util.Arrays;

public class n_11053 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[n], dp[]=new int[n];
        Arrays.fill(dp, 1);
        String st[]=br.readLine().split(" ");
        for(int i=0; i<n; i++)
            arr[i]=Integer.parseInt(st[i]);
        for(int i=1; i<n; i++){
            for(int j=0; j<i; j++){
                if(arr[j]<arr[i])
                    dp[i]=Math.max(dp[i],dp[j]+1);
            }
        }
        Arrays.sort(dp);
        System.out.println(dp[n-1]);
    }
}
