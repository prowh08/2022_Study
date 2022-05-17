package Study_2022.baekjoon.shim.Java.알고리즘_분류.문자열;

import java.util.*;

public class n_10809 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String st=sc.nextLine();
        int arr[]=new int[26];
        Arrays.fill(arr, -1);
        for(int i=0; i<st.length(); i++){
            if(arr[st.charAt(i)-'a']==-1)
                arr[st.charAt(i)-'a']=i;
        }
        for(int i=0; i<26; i++)
            System.out.print(arr[i]+" ");
    }
}
