package Study_2022.baekjoon.shim.Java.알고리즘_분류.문자열;

import java.util.*;

public class n_1152 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String st[]=sc.nextLine().split(" ");
        int len=st.length;
        for(int i=0; i<st.length; i++){
            if(st[i]=="")
                len--;
        }
        System.out.println(len);
    }
}
