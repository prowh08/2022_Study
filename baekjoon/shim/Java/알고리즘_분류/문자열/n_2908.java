package Study_2022.baekjoon.shim.Java.알고리즘_분류.문자열;

import java.util.*;

public class n_2908 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String st=sc.nextLine();
        StringBuffer sb=new StringBuffer(st);
        String reverse[]=sb.reverse().toString().split(" ");
        System.out.println(Math.max(Integer.parseInt(reverse[0]), Integer.parseInt(reverse[1])));
    }
}
