package Study_2022.baekjoon.shim.Java.알고리즘_분류.문자열;

import java.util.*;

public class n_5622 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String st=sc.nextLine();
        int sum=0, len=st.length();
        for(int i=0; i<len; i++){
            int ch=st.charAt(i)-65;
            if(ch>17)
                ch-=(ch==25?2:1);
            sum+=ch/3;
        }
        System.out.println(3*len+sum);
    }
}
