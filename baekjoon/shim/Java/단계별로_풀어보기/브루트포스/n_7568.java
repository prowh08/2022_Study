package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.브루트포스;

import java.io.*;

public class n_7568 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(br.readLine()), arr[][]=new int[T][2];
        for(int i=0; i<T; i++){
            String st[]=br.readLine().split(" ");
            arr[i][0]=Integer.parseInt(st[0]);
            arr[i][1]=Integer.parseInt(st[1]);
        }
        for(int i=0; i<T; i++){
            int r=1;
            for(int j=0; j<T; j++){
                if(i==j)
                    continue;
                if(arr[i][0]<arr[j][0]&&arr[i][1]<arr[j][1])
                    r++;
            }
            System.out.print(r+" ");
        }
    }
}
