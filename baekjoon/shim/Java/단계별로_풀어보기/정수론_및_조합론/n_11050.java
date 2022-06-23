package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정수론_및_조합론;

import java.util.*;

public class n_11050 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), m=sc.nextInt(), result=1;
        for(int i=n; i>Math.max(m,n-m); i--)
            result*=i;
        for(int i=2; i<=Math.min(m,n-m); i++)
            result/=i;
        System.out.println(result);
    }
}
