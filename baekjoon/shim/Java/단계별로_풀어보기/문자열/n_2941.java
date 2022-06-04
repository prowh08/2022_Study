package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.문자열;

import java.util.*;

public class n_2941{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String st=sc.nextLine();
        String[] l={"c=","c-","dz=","d-","lj","nj","s=","z="};
        for(int i=0; i<l.length; i++)
            st=st.replace(l[i], ".");
        System.out.println(st.length());
    }
}