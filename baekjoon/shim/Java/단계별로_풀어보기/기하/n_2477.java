package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기하;

import java.io.*;

public class n_2477 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[6];
        int w=0, h=0, w2=0, h2=0;
        for(int i=0; i<6; i++){
            String st[]=br.readLine().split(" ");
            arr[i]=Integer.parseInt(st[1]);
            if(i%2==0)
                w=Math.max(w,arr[i]);
            else
                h=Math.max(h,arr[i]);
        }
        for(int i=0; i<6; i++){
            if(i%2==0 && h==arr[(i+5)%6]+arr[(i+1)%6])
                w2=arr[i];
            else if(i%2==1 && w==arr[(i+5)%6]+arr[(i+1)%6])
                h2=arr[i];
        }
        System.out.println(n*(w*h-w2*h2));
    }
}
