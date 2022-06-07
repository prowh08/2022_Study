package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정렬;

import java.io.*;
import java.util.*;

public class n_2751 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[n];
        for(int i=0; i<n; i++)
            arr[i]=Integer.parseInt(br.readLine());
        Arrays.sort(arr);
        for(int i=0; i<n; i++)
            bw.write(arr[i]+"\n");
        bw.flush();
        bw.close();
    }
}