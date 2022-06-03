package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.문자열;

import java.util.*;

public class n_1157 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String st=sc.nextLine().toUpperCase();
        int arr[]=new int[26], max=0, max_i=0;
        boolean t=false;
        for(int i=0; i<st.length(); i++)
            arr[st.charAt(i)-'A']++;
        for(int i=0; i<26; i++){
            if(arr[i]>max) {
                max=arr[i];
                max_i=i;
                t=false;
            }else if(arr[i]==max)
                t=true;
        }
        System.out.println(t?"?":(char)(max_i+'A'));
    }
}
