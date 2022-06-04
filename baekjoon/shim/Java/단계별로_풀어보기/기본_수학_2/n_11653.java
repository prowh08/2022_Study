package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기본_수학_2;

import java.util.*;

public class n_11653 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), i=2;
        while(i<=n){
            if(n%i==0){
                System.out.println(i);
                n/=i;
            }else i++;
        }
    }
}
