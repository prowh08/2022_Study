package Study_2022.baekjoon.shim.Java.알고리즘_분류.기본_수학_1;

import java.util.*;

public class n_1193 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), t=1, b=1, count=0,l=0;
        while(count<n){
            l++;
            count=l*(l+1)/2;
        }
        if(l%2==0){
            t=l-(count-n);
            b=count-n+1;
        }else{
            t=count-n+1;
            b=l-(count-n);
        }
        System.out.println(t+"/"+b);
    }
}
