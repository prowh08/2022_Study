package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.util.*;

public class n_10844 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        long arr[][]=new long[n+1][10], result=0;
        for(int i=1; i<10; i++)
            arr[1][i]=1;
        for(int i=2; i<=n; i++){
            for(int j=0; j<10; j++){
                if(j==0)
                    arr[i][j]=arr[i-1][j+1];
                else if(j==9)
                    arr[i][j]=arr[i-1][j-1];
                else
                    arr[i][j]=arr[i-1][j+1]+arr[i-1][j-1];
                arr[i][j]%=1000000000;
            }
        }
        for(int i=0; i<10; i++)
            result+=arr[n][i];
        System.out.println(result%1000000000);
    }
}