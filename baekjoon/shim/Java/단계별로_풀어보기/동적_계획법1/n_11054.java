package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.io.*;
import java.util.*;

public class n_11054 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[n], dp[]=new int[n], dp2[]=new int[n];
        String st[]=br.readLine().split(" ");
        for(int i=0; i<n; i++)
            arr[i]=Integer.parseInt(st[i]);
        Arrays.fill(dp,1);
        for(int i=1; i<n; i++){
            for(int j=0; j<i; j++){
                if(arr[j]<arr[i])
                    dp[i]=Math.max(dp[i],dp[j]+1);
            }
        }
        for(int i=n-2; i>=0; i--){
            for(int j=n-1; j>i; j--){
                if(arr[j]<arr[i])
                    dp2[i]=Math.max(dp2[i],dp2[j]+1);
            }
        }
        for(int i=0; i<n; i++)
            dp[i]+=dp2[i];
        Arrays.sort(dp);
        System.out.println(dp[n-1]);
    }
}
