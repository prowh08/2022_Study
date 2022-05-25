package Study_2022.baekjoon.shim.Java.알고리즘_분류.기본_수학_1;

import java.util.*;

public class n_2839 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), count=0;
        while(true){
            if(n<0) {
                System.out.println(-1);
                break;
            }
            if(n%5==0){
                count+=n/5;
                System.out.println(count);
                break;
            }else{
                n-=3;
                count++;
            }
        }
    }
}
