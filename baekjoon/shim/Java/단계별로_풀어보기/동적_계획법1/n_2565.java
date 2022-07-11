package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.io.*;
import java.util.*;

public class n_2565 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine()), arr[][]=new int[n][2], dp[]=new int[n];
        Arrays.fill(dp,1);
        for(int i=0; i<n; i++){
            String st[]=br.readLine().split(" ");
            arr[i][0]=Integer.parseInt(st[0]);
            arr[i][1]=Integer.parseInt(st[1]);
        }
        Arrays.sort(arr,new Comparator<int[]>(){
            @Override
            public int compare(int[] o1,int[] o2){
                return o1[0]-o2[0];
            }
        });
        for(int i=1; i<n; i++){
            for(int j=0; j<i; j++){
                if(arr[j][1]<arr[i][1])
                    dp[i]=Math.max(dp[i],dp[j]+1);
            }
        }
        Arrays.sort(dp);
        System.out.println(n-dp[n-1]);
    }
}