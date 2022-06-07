package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정렬;

import java.io.*;

public class n_10989 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[10001];
        for(int i=0; i<n; i++)
            arr[Integer.parseInt(br.readLine())]++;
        for(int i=0; i<10001; i++){
            while(arr[i]>0){
                bw.write(i+"\n");
                arr[i]--;
            }
        }
        bw.flush();
        bw.close();
    }
}
