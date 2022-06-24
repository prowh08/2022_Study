package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정수론_및_조합론;

import java.util.*;

public class n_1676 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int c=n/10, f=n/125+n/25;
        System.out.println(n%10<5?c*2+f:c*2+1+f);
    }
}
