package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.그리디_알고리즘;

import java.io.*;

public class n_13305 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        String st[]=br.readLine().split(" "), st1[]=br.readLine().split(" ");
        long min=Long.parseLong(st1[0]), sum=Long.parseLong(st[0])*min;
        for(int i=1; i<n-1; i++){
            int num=Integer.parseInt(st1[i]);
            if(num<min)
                min=num;
            sum+=min*Integer.parseInt(st[i]);
        }
        System.out.println(sum);
    }
} 