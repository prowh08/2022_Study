package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.문자열;

import java.util.*;
public class n_11720 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), sum=0;
        String l=sc.nextLine(), st[]=sc.nextLine().split("");
        for(int i=0; i<n; i++)
            sum+=Integer.parseInt(st[i]);
        System.out.println(sum);
    }
}
