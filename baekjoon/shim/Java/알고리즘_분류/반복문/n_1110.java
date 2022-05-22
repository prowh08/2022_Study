package Study_2022.baekjoon.shim.Java.알고리즘_분류.반복문;

import java.util.*;

public class n_1110 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), num=n, count=0;
        while(true){
            num=((num%10)*10+((num/10)+(num%10))%10);
            count++;
            if(n==num){
                System.out.println(count);
                break;
            }
        }
    }
}
