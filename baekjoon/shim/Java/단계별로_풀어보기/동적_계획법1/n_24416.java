package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.util.*;

public class n_24416 {
    public static int a=0, b=0;
    public static int arr[];
    public static int fib(int n){
        if(n==1 ||n==2){
            a++;
            return 1;
        }
        return fib(n-1)+fib(n-2);
    }
    public static int fib2(int n){
        arr[1]=1;
        arr[2]=1;
        for(int i=3; i<=n; i++){
            arr[i]=arr[i-1]+arr[i-2];
            b++;
        }
        return arr[n];
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt();
        arr=new int[T+1];
        fib(T);
        fib2(T);
        System.out.println(a+" "+b);
    }
}
