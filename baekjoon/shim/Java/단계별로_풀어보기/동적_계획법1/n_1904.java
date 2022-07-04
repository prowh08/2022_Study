package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.util.*;

public class n_1904 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        if(n==1||n==2)
            System.out.println(n);
        else{
            int arr[]=new int[n+1];
            arr[1]=1;
            arr[2]=2;
            for(int i=3; i<=n; i++)
                arr[i]=(arr[i-1]+arr[i-2])%15746;
            System.out.println(arr[n]);
        }
    }
}
