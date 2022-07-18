package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.그리디_알고리즘;

import java.io.*;

public class n_11047 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String st[]=br.readLine().split(" ");
        int n1=Integer.parseInt(st[0]), n2=Integer.parseInt(st[1]);
        int arr[]=new int[n1], sum=0;
        for(int i=0; i<n1; i++)
            arr[i]=Integer.parseInt(br.readLine());
        for(int i=n1-1; i>=0; i--){
            sum+=n2/arr[i];
            n2%=arr[i];
        }
        System.out.println(sum);
    }
}
