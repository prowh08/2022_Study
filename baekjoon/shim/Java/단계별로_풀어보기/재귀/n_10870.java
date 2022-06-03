package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.재귀;

import java.util.*;

public class n_10870 {
    public static int Fibo(int n){
        if(n>=2)
            n=Fibo(n-1)+Fibo(n-2);
        return n;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println(Fibo(n));
    }
}
