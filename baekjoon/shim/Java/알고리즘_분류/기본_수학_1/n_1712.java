package Study_2022.baekjoon.shim.Java.알고리즘_분류.기본_수학_1;

import java.util.*;

public class n_1712 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int arr[]=new int[3];
        for(int i=0; i<3; i++)
            arr[i]=sc.nextInt();
        System.out.println(arr[1]<arr[2]?arr[0]/(arr[2]-arr[1])+1:-1);
    }
}