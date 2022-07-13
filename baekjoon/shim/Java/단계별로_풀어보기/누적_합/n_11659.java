package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.누적_합;

import java.io.*;

public class n_11659 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        String st[]=br.readLine().split(" "), st2[]=br.readLine().split(" ");
        int arr[]=new int[Integer.parseInt(st[0])+1];
        arr[1]=Integer.parseInt(st2[0]);
        for(int i=2; i<arr.length; i++)
            arr[i]+=arr[i-1]+Integer.parseInt(st2[i-1]);
        for(int i=0; i<Integer.parseInt(st[1]); i++){
            String str[]=br.readLine().split(" ");
            bw.write(arr[Integer.parseInt(str[1])]-arr[Integer.parseInt(str[0])-1]+"\n");
        }
        bw.flush();bw.close();
    }
}