package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.util.*;

public class n_1463 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n+1];
        arr[0]=arr[1]=0;
        for(int i=2; i<=n; i++){
            arr[i]=arr[i-1]+1;
            if(i%3==0)
                arr[i]=Math.min(arr[i],arr[i/3]+1);
            if(i%2==0)
                arr[i]=Math.min(arr[i],arr[i/2]+1);
        }
        System.out.println(arr[n]);
    }
}
