package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기본_수학_2;

import java.util.*;

public class n_2581 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n1=sc.nextInt(), n2=sc.nextInt(), sum=0, min=0;
        for(int i=n1; i<=n2; i++){
            int count=0;
            for(int j=2; j<=Math.sqrt(i); j++){
                if(i%j==0) count++;
            }
            if(count==0&&i!=1){
                if(min==0)min=i;
                sum+=i;
            }
        }
        System.out.println(sum==0?-1:(sum+"\n"+min));
    }
}
