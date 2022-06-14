package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.집합과_맵;

import java.util.*;

public class n_11478 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String st=sc.nextLine();
        int count=1;
        HashSet<String>set=new HashSet<>();
        while(count<=st.length()){
            for(int i=0; i<st.length()-count+1; i++)
                set.add(st.substring(i, i+count));
            count++;
        }
        System.out.println(set.size());
    }
}
