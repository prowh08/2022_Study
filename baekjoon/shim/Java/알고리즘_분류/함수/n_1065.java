package Study_2022.baekjoon.shim.Java.알고리즘_분류.함수;

import java.util.*;

public class n_1065{
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), count=0;
        for(int i=100; i<=n; i++){
            int n1=i/100;
            int n2=(i%100)/10;
            int n3=(i%100)%10;
            if(n1-n2==n2-n3) count++;
        }
        System.out.println((n<100?n:99)+count);
    }
}
