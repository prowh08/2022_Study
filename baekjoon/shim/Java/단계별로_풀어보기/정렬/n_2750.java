package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정렬;

import java.io.*;

public class n_2750 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[n];
        for(int i=0; i<n; i++)
            arr[i]=Integer.parseInt(br.readLine());
        for(int i=0; i<n-1; i++){
            for(int j=i+1; j<n; j++){
                if(arr[i]>arr[j]){
                    int num=arr[j];
                    arr[j]=arr[i];
                    arr[i]=num;
                }
            }
        }
        for(int i=0; i<n; i++)
            bw.write(arr[i]+"\n");
        bw.flush();
        bw.close();
    }
}
