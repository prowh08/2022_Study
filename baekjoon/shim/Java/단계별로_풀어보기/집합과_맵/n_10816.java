package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.집합과_맵;

import java.io.*;
import java.util.*;

public class n_10816 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        String st[]=br.readLine().split(" ");
        HashMap<String,Integer>map=new HashMap<>();
        for(int i=0; i<n; i++)
            map.put(st[i],map.getOrDefault(st[i],0)+1);
        int m=Integer.parseInt(br.readLine());
        String st2[]=br.readLine().split(" ");
        for(int i=0; i<m; i++)
            bw.write((map.get(st2[i])==null? 0: map.get(st2[i])) +" ");
        bw.flush();bw.close();
    }
}
