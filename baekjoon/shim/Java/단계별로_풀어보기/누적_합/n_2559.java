package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.누적_합;

import java.io.*;
import java.util.*;

public class n_2559 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String st1[]=br.readLine().split(" ");
        int n1=Integer.parseInt(st1[0]), n2=Integer.parseInt(st1[1]);
        String st2[]=br.readLine().split(" ");
        int arr[]=new int[n1+1];
        ArrayList<Integer>list=new ArrayList<>();
        for(int i=1; i<=n1; i++){
            arr[i]=Integer.parseInt(st2[i-1])+arr[i-1];
            if(i>=n2)
                list.add(arr[i]-arr[i-n2]);
        }
        Collections.sort(list);
        System.out.println(list.get(list.size()-1));
    }
}
