package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.재귀;

import java.util.*;

public class n_10872 {
    public static int fac(int n){
        if(n<=1)
            return 1;
        return fac(n-1)*n;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println(fac(n));
    }
}
