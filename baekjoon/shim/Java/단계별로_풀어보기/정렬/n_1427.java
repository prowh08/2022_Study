package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정렬;

import java.util.*;

public class n_1427 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String st[]=sc.nextLine().split("");
        Integer arr[]=new Integer[st.length];
        for(int i=0; i<st.length; i++)
            arr[i]=Integer.parseInt(st[i]);
        Arrays.sort(arr,Collections.reverseOrder());
        for(int i=0; i<st.length; i++)
            System.out.print(arr[i]);
    }
}
