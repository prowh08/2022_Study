package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기본_수학_2;

import java.util.*;

public class n_1978 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt(), answer=0;
        for(int i=0; i<T; i++){
            int n=sc.nextInt(), count=0;
            if(n==1) continue;
            for(int j=2; j<=Math.sqrt(n); j++){
                if(n%j==0) count++;
            }
            if(count==0) answer++;
        }
        System.out.println(answer);
    }
}
