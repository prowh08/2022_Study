package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.브루트포스;

import java.util.*;

public class n_1436 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(),c=665;
        while(n>0){
            c++;
            if(Integer.toString(c).contains("666"))
                n--;
        }
        System.out.print(c);
    }
}