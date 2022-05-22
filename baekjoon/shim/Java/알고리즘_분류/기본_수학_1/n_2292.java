package Study_2022.baekjoon.shim.Java.알고리즘_분류.기본_수학_1;

import java.util.*;

public class n_2292 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), sum=2, answer=1;
        if(n==1)
            System.out.println(1);
        else{
            while(true){
                if((sum+=6*answer)>n){
                    System.out.println(answer+1);
                    break;
                }
                answer+=1;
            }
        }
    }
}