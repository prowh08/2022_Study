package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.브루트포스;

import java.util.*;

public class n_2231 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), answer=0;
        for(int i=n; i>0; i--){
            int sum=0;
            String num=Integer.toString(i);
            for(int j=0; j<num.length(); j++)
                sum+=num.charAt(j)-'0';
            if(i+sum==n)
                answer=i;
        }
        System.out.println(answer);
    }
}
