package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정수론_및_조합론;

import java.io.*;
import java.util.*;

public class n_9375 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            HashMap<String,Integer>map=new HashMap<>();
            int T=Integer.parseInt(br.readLine());
            for(int j=0; j<T;j++){
                String st[]=br.readLine().split(" ");
                map.put(st[1], map.getOrDefault(st[1], 0)+1);
            }
            int answer=1;
            for(String key:map.keySet())
                answer*=(map.get(key)+1);
            bw.write(answer-1+"\n");
        }
        bw.flush();bw.close();
    }
}
