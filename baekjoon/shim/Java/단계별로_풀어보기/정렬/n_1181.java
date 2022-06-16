package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정렬;

import java.io.*;
import java.util.*;

public class n_1181 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        String st[]=new String[n];
        for(int i=0; i<n; i++)
            st[i]=br.readLine();
        Arrays.sort(st, (o1, o2) -> {
            if(o1.length()==o2.length())
                return o1.compareTo(o2);
            else
                return o1.length()-o2.length();
        });
        bw.write(st[0]+"\n");
        for(int i=1; i<n; i++){
            if(!st[i].equals(st[i-1]))
                bw.write(st[i]+"\n");
        }
        bw.flush();bw.close();
    }
}
