package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정렬;

import java.io.*;
import java.util.*;

public class n_11650 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine()), arr[][]=new int[n][2];
        for(int i=0; i<n; i++){
            String st[]=br.readLine().split(" ");
            arr[i][0]=Integer.parseInt(st[0]);
            arr[i][1]=Integer.parseInt(st[1]);
        }
        Arrays.sort(arr,new Comparator<int[]>() {
            @Override
            public int compare(int[] o1,int[] o2){
                if(o1[0]==o2[0])
                    return o1[1]-o2[1];
                else
                    return o1[0]-o2[0];
            }
        });
        for(int i=0; i<n; i++)
            bw.write(arr[i][0]+" "+arr[i][1]+"\n");
        bw.flush();bw.close();
    }
}
