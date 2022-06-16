package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기하;

import java.util.*;

public class n_1085 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String st[]=sc.nextLine().split(" ");
        int arr[]=new int[st.length];
        for(int i=0; i<st.length; i++)
            arr[i]=Integer.parseInt(st[i]);
        System.out.println(Math.min(Math.min(arr[0],arr[2]-arr[0]),Math.min(arr[1],arr[3]-arr[1])));
    }
}
