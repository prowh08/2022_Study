package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기하;

import java.io.*;
import java.util.*;

public class n_4153 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        while(true){
            String str[]=br.readLine().split(" ");
            int arr[]=new int[3];
            for(int i=0; i<3; i++)
                arr[i]=Integer.parseInt(str[i]);
            Arrays.sort(arr);
            if(arr[2]==0)
                break;
            bw.write(Math.pow(arr[2],2)==Math.pow(arr[1], 2)+Math.pow(arr[0], 2)?"right\n":"wrong\n");
        }
        bw.flush();bw.close();
    }
}
