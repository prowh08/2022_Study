package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.그리디_알고리즘;

import java.io.*;
import java.util.*;

public class n_11399 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[n], sum=0;
        String st[]=br.readLine().split(" ");
        for(int i=0; i<n; i++)
            arr[i]=Integer.parseInt(st[i]);
        Arrays.sort(arr);
        for(int i=0;i<n; i++)
            sum+=arr[i]*(n-i);
        System.out.println(sum);
    }
}
