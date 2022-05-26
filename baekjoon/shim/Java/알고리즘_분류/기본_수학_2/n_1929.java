package Study_2022.baekjoon.shim.Java.알고리즘_분류.기본_수학_2;

import java.util.*;

public class n_1929 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n1=sc.nextInt(), n2=sc.nextInt();
        for(int i=n1; i<=n2; i++){
            int count=0;
            if(i==1) continue;
            for(int j=2; j<=Math.sqrt(i); j++){
                if(i%j==0){
                    count++;
                    break;
                }
            }
            if(count==0)
                System.out.println(i);
        }
    }
}
