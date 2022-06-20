package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기하;

import java.io.*;

public class n_1358 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String st[]=br.readLine().split(" ");
        int c=0, arr[]=new int[st.length];
        for(int i=0; i<st.length; i++)
            arr[i]=Integer.parseInt(st[i]);
        for(int i=0; i<arr[4]; i++){
            String str[]=br.readLine().split(" ");
            int n1=Integer.parseInt(str[0]),n2=Integer.parseInt(str[1]);
            if(arr[2]<=n1&&n1<=arr[2]+arr[0]&&arr[3]<=n2&&n2<=arr[3]+arr[1]){
                c++;
                continue;
            }
            double d1=Math.pow(Math.pow(n1-arr[2],2)+Math.pow(n2-arr[3]-arr[1]/2,2),0.5);
            double d2=Math.pow(Math.pow(n1-arr[2]-arr[0],2)+Math.pow(n2-arr[3]-arr[1]/2,2),0.5);
            if(d1<=arr[1]/2||d2<=arr[1]/2)
                c++;           
        }
        System.out.println(c);
    }
}
