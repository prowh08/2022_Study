package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.집합과_맵;

import java.io.*;
import java.util.Arrays;

public class n_10815 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[n];
        String st[]=br.readLine().split(" ");
        for(int i=0; i<n; i++)
            arr[i]=Integer.parseInt(st[i]);
        Arrays.sort(arr);
        int m=Integer.parseInt(br.readLine()), arr2[]=new int[m];
        String st2[]=br.readLine().split(" ");
        for(int i=0;i<m; i++)
            arr2[i]=Integer.parseInt(st2[i]);
        for(int i=0; i<m; i++){
            int max=n-1, min=0, middle=0;
            boolean b=false;
            while(max>=min){
                middle=(max+min)/2;
                if(arr[middle]>arr2[i])
                    max=middle-1;
                else if(arr[middle]<arr2[i])
                    min=middle+1;
                else{
                    bw.write(1+" ");
                    b=true;
                    break;
                }
            }
            if(b==false) bw.write(0+" ");
        }
        bw.flush();
        bw.close();
    }
}