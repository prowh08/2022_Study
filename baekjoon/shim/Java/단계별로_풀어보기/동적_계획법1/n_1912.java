package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.동적_계획법1;

import java.io.*;

public class n_1912 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(br.readLine());
        int arr[]=new int[T], sum=0;
        String st[]=br.readLine().split(" ");
        for(int i=0; i<T; i++)
            arr[i]=Integer.parseInt(st[i]);
        int max=arr[0];
        for(int i=0; i<T; i++){
            sum+=arr[i];
            max=Math.max(sum, max);
            if(sum<0){
                sum=0;
            }
        }
        System.out.println(max);
    }
}
