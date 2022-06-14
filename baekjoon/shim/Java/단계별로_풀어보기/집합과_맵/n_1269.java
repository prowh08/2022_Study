package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.집합과_맵;

import java.io.*;
import java.util.*;

public class n_1269 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String st[]=br.readLine().split(" ");
        String st1[]=br.readLine().split(" "), st2[]=br.readLine().split(" ");
        HashSet<String>set=new HashSet<>();
        int count=0;
        for(int i=0; i<st1.length; i++)
            set.add(st1[i]);
        for(int i=0; i<st2.length; i++){
            if(set.contains(st2[i]))
            count++;
        }
        System.out.println(Integer.parseInt(st[0])+Integer.parseInt(st[1])-count*2);
    }
}
